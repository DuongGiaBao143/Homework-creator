"""Tạo bản PDF nhẹ, giữ nguyên bản gốc; kiểm tra chữ, ảnh và nét vector sau nén."""
from pathlib import Path
from hashlib import sha256
import pymupdf

root = Path(__file__).resolve().parent.parent / 'Output'
destination = root / 'PDF_Nhe'
assert not destination.exists(), 'PDF_Nhe đã tồn tại; không ghi đè bản đang có.'
sources = sorted(p for p in root.rglob('*.pdf') if 'PDF_Nhe' not in p.parts)
assert sources, 'Không tìm thấy PDF trong Output.'
destination.mkdir()
qa = destination / '_qa'
qa.mkdir()
rows, seen_images, previews = [], set(), []
cache = {}

for source in sources:
    original = source.read_bytes()
    digest = sha256(original).hexdigest()
    # Các đề này có đồ thị/hình học dạng bitmap, giữ độ phân giải và chất lượng cao hơn.
    dpi, quality = (300, 95) if source.parent.name in {f'De {n}' for n in range(4, 10)} else (200, 90)
    output = destination / source.relative_to(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(stream=original, filetype='pdf') as before:
        if digest in cache:
            compressed = cache[digest]
        else:
            with pymupdf.open(stream=original, filetype='pdf') as working:
                if any(page.get_image_info() for page in working):
                    working.rewrite_images(dpi_threshold=round(dpi*1.25), dpi_target=dpi,
                                           quality=quality, bitonal=False)
                candidate = working.tobytes(garbage=4, deflate=True, use_objstms=1)
            compressed = candidate if len(candidate) < len(original) else original
            cache[digest] = compressed
        with pymupdf.open(stream=compressed, filetype='pdf') as after:
            assert len(before) == len(after), f'Sai số trang: {source}'
            for number, (a, b) in enumerate(zip(before, after), 1):
                assert a.rect == b.rect and a.rotation == b.rotation
                assert a.get_text() == b.get_text(), f'Sai chữ trang {number}: {source}'
                assert a.get_drawings() == b.get_drawings(), f'Sai nét vector trang {number}: {source}'
                old_images, new_images = a.get_image_info(xrefs=True), b.get_image_info(xrefs=True)
                assert len(old_images) == len(new_images), f'Thiếu hình trang {number}: {source}'
                assert [i['bbox'] for i in old_images] == [i['bbox'] for i in new_images]
                if not old_images:
                    assert a.get_pixmap().samples == b.get_pixmap().samples, f'Sai render trang {number}: {source}'
                for image in old_images:
                    key = sha256(before.xref_stream_raw(image['xref']) or b'').hexdigest() if image['xref'] else str(image['bbox'])
                    if key in seen_images:
                        continue
                    seen_images.add(key)
                    box = pymupdf.Rect(image['bbox']) & a.rect
                    if box.is_empty:
                        continue
                    label = f'{source.relative_to(root)} - trang {number}'
                    idx = len(previews)+1
                    for tag, page in [('goc', a), ('nhe', b)]:
                        page.get_pixmap(matrix=pymupdf.Matrix(2, 2), clip=box, alpha=False).save(qa/f'{idx:03d}_{tag}.png')
                    previews.append((idx, label))
        output.write_bytes(compressed)
        with pymupdf.open(output) as reopened:
            assert len(reopened) == len(before)
        assert sha256(source.read_bytes()).hexdigest() == digest, 'File gốc đã bị thay đổi.'
        rows.append((str(source.relative_to(root)), len(original), len(compressed), len(before), dpi, quality))
        print(f'{source.parent.name}/{source.name}: {len(original)/1048576:.2f} -> {len(compressed)/1048576:.2f} MB', flush=True)

from PIL import Image, ImageOps, ImageDraw
for start in range(0, len(previews), 8):
    canvas = Image.new('RGB', (1600, 1560), '#e8e8e8')
    draw = ImageDraw.Draw(canvas)
    for slot, (idx, label) in enumerate(previews[start:start+8]):
        x, y = (slot % 2)*800, (slot // 2)*390
        draw.text((x+10, y+5), label, fill='black')
        for column, tag in enumerate(['goc', 'nhe']):
            with Image.open(qa/f'{idx:03d}_{tag}.png') as im:
                tile = ImageOps.contain(im, (385, 340))
                canvas.paste(tile, (x+column*400+7+(385-tile.width)//2, y+40+(340-tile.height)//2))
            draw.text((x+column*400+10, y+23), tag, fill='black')
    canvas.save(qa/f'compare_{start//8+1:02d}.png')

total_before = sum(r[1] for r in rows)
total_after = sum(r[2] for r in rows)
report = ['# Kết quả tạo PDF nhẹ', '',
          f'- {len(rows)} PDF: {total_before/1048576:.2f} MB → {total_after/1048576:.2f} MB; giảm {(1-total_after/total_before)*100:.1f}%.',
          '- Bản gốc giữ nguyên. Các bản nhẹ đã được mở lại để kiểm tra.',
          '- Số trang, chữ, số lượng/vị trí ảnh và nét vector giữ nguyên; các trang không có ảnh khớp render từng pixel.',
          '- Đề 4–9: ảnh 300 DPI/JPEG 95%; các đề khác: 200 DPI/JPEG 90%. Giữ ảnh đơn sắc nguyên dạng, không chuyển trang thành ảnh.',
          '- Không bảo đảm giữ từng pixel của ảnh được nén; cần xem bảng so sánh trước khi chốt chất lượng in.', '',
          '| PDF | Gốc (MB) | Nhẹ (MB) | Giảm | Trang |', '|---|---:|---:|---:|---:|']
for name, old, new, pages, dpi, quality in rows:
    report.append(f'| {name} | {old/1048576:.2f} | {new/1048576:.2f} | {(1-new/old)*100:.1f}% | {pages} |')
(destination/'BAO_CAO.md').write_text('\n'.join(report)+'\n', encoding='utf-8')
print(f'OK: {len(rows)} files, {len(previews)} unique-image comparisons, {total_before/1048576:.2f} -> {total_after/1048576:.2f} MB.', flush=True)
