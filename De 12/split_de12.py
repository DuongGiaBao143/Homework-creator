"""Tách bản đã biên dịch và kiểm tra lại hai PDF trước khi xuất bản."""
from pathlib import Path
import re
from pypdf import PdfReader, PdfWriter

base = Path(__file__).resolve().parent
reader = PdfReader(base / 'De 12.pdf')
texts = [p.extract_text() or '' for p in reader.pages]
markers = [i for i, text in enumerate(texts) if 'BẢNG ĐÁP ÁN TỔNG HỢP' in text]
assert len(markers) == 1, 'Phải có đúng một trang bắt đầu bảng đáp án.'
split = markers[0]
assert 0 < split < len(reader.pages)-1
assert 'HƯỚNG DẪN GIẢI CHI TIẾT' in texts[split+1]
questions = re.findall(r'Câu\s+(\d+)\s*:', '\n'.join(texts[:split]))
assert list(map(int, questions)) == list(range(1, 13))+list(range(1, 5))+list(range(1, 7))
assert 'HẾT' in texts[split-1]
for filename, start, end, title in [
    ('12.pdf', 0, split, 'De thi so 12 - Ma de 0012'),
    ('12_Ans.pdf', split, len(reader.pages), 'Dap an va loi giai de so 12'),
]:
    writer = PdfWriter()
    for page in reader.pages[start:end]:
        writer.add_page(page)
    writer.add_metadata({'/Title': title, '/Author': 'Duong Gia Bao'})
    path = base / filename
    with path.open('wb') as output:
        writer.write(output)
    check = PdfReader(path)
    assert len(check.pages) == end-start
    content = '\n'.join(p.extract_text() or '' for p in check.pages)
    if start == 0:
        assert 'BẢNG ĐÁP ÁN TỔNG HỢP' not in content
        assert 'HƯỚNG DẪN GIẢI CHI TIẾT' not in content
    else:
        assert 'BẢNG ĐÁP ÁN TỔNG HỢP' in content
        assert 'HƯỚNG DẪN GIẢI CHI TIẾT' in content
        for answer in ['54,8', '0,66', '16,2', '7,3', '441,6', '1328']:
            assert answer in content.replace(' ', '')
    print(f'[OK] {path.name}: {len(check.pages)} trang')
assert len(PdfReader(base/'12.pdf').pages)+len(PdfReader(base/'12_Ans.pdf').pages) == len(reader.pages)
print('[OK] De tach dung 22 cau, khong lo dap an; loi giai day du.')
