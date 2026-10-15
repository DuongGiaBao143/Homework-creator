"""Tách và kiểm tra PDF demo trong thư mục hiện tại, không xuất bản ra PRIVATE."""
from pathlib import Path
import re
from pypdf import PdfReader, PdfWriter

base = Path(__file__).resolve().parent
reader = PdfReader(base/'Demo.pdf')
texts = [p.extract_text() or '' for p in reader.pages]
markers = [i for i, text in enumerate(texts) if 'BẢNG ĐÁP ÁN TỔNG HỢP' in text]
assert len(markers) == 1
split = markers[0]
assert 0 < split < len(texts)-1
assert 'HƯỚNG DẪN GIẢI CHI TIẾT' in texts[split+1]
assert list(map(int, re.findall(r'Câu\s+(\d+)\s*:', '\n'.join(texts[:split])))) == list(range(1, 13))+list(range(1, 5))+list(range(1, 7))
assert 'HẾT' in texts[split-1]
for filename, start, stop, title in [
    ('De_demo.pdf', 0, split, 'De demo phan loai - Ban xem truoc'),
    ('Dap_an_demo.pdf', split, len(texts), 'Dap an va loi giai - De demo phan loai'),
]:
    writer = PdfWriter()
    for page in reader.pages[start:stop]:
        writer.add_page(page)
    writer.add_metadata({'/Title': title, '/Author': 'Duong Gia Bao'})
    output = base/filename
    with output.open('wb') as stream:
        writer.write(stream)
    check = PdfReader(output)
    assert len(check.pages) == stop-start
    content = '\n'.join(p.extract_text() or '' for p in check.pages)
    if start == 0:
        assert 'BẢNG ĐÁP ÁN TỔNG HỢP' not in content and 'HƯỚNG DẪN GIẢI CHI TIẾT' not in content
    else:
        assert 'BẢNG ĐÁP ÁN TỔNG HỢP' in content and 'HƯỚNG DẪN GIẢI CHI TIẾT' in content
        assert all(value in content.replace(' ', '') for value in ['2,91', '0,46', '19,7', '0,92', '4,39', '12,0'])
    print(f'[OK] {filename}: {len(check.pages)} trang')
assert len(PdfReader(base/'De_demo.pdf').pages)+len(PdfReader(base/'Dap_an_demo.pdf').pages) == len(reader.pages)
log = (base/'Demo.log').read_text(errors='ignore')
assert 'Overfull' not in log and 'Undefined control sequence' not in log
print('[OK] Du 22 cau, khong lo dap an, ban loi giai co du ket qua; khong tran le.')
