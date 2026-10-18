"""Chuẩn hóa MathType/VNI, tái sử dụng nguyên bản từ bộ lớp 12."""
import re


MATHTYPE_SYMBOL_MAP = {
    0xf028: '(', 0xf029: ')', 0xf02b: '+', 0xf02d: '-', 0xf03d: '=',
    0xf03c: '<', 0xf03e: '>', 0xf02f: '/', 0xf03a: ':', 0xf03b: ';',
    0xf05b: '[', 0xf05d: ']', 0xf07b: '{', 0xf07d: '}',
    0xf0e9: '[', 0xf0ea: '[', 0xf0eb: '[',
    0xf0f9: ']', 0xf0fa: ']', 0xf0fb: ']',
    0xf0e6: '(', 0xf0e7: '(', 0xf0e8: '(',
    0xf0f6: ')', 0xf0f7: ')', 0xf0f8: ')',
    0xf0ec: '{', 0xf0ed: '{', 0xf0ee: '{', 0xf0ef: '{',
    0xf0fc: '}', 0xf0fd: '}', 0xf0fe: '}',
    0xf8f1: '{', 0xf8f2: '{', 0xf8f3: '{', 0xf8f4: '|',
    0xf0a2: "'", 0x2032: "'", 0x2212: '-',
    0xf070: 'pi', 0xf0a5: ' vô cùng ', 0xf0b0: '°',
    0xf0a3: '<=', 0xf0b3: '>=', 0xf0b9: '!=', 0xf0bb: '~=',
    0xf0de: ' => ', 0xf0db: ' <=> ', 0xf0ae: ' -> ',
    0xf0b7: ' · ', 0xf0d7: ' × ', 0xf0f2: ' tích phân ',
    0xf0a1: ' R ', 0xf0ce: ' Z ', 0xf057: ' Omega ',
    0xf044: ' Delta ', 0xf05e: ' vuông góc ', 0xf0d8: ' góc ',
    0xf055: ' hợp ', 0xf0c7: ' giao ',
    0xf061: ' alpha ', 0xf062: ' beta ', 0xf06f: ' omega ',
    0xf063: '[ ]', 0xf040: ' ', 0xf075: '', 0xf072: ''
}


VNI_COMMON_MAP = {
    "Nguyeãn Tieán Haø": "Nguyễn Tiến Hà",
    "Nguyeãn": "Nguyễn", "Tieán": "Tiến", "Haø": "Hà",
    "phöông trình": "phương trình", "baát phöông trình": "bất phương trình",
    "heä phöông trình": "hệ phương trình",
    "löôïng giaùc": "lượng giác", "cô baûn": "cơ bản",
    "ñaïo haøm": "đạo hàm", "nguyeân haøm": "nguyên hàm", "tích phaân": "tích phân",
    "ñoà thò": "đồ thị", "haøm soá": "hàm số", "hàm soá": "hàm số",
    "bieán thieân": "biến thiên", "ñoàng bieán": "đồng biến", "nghòch bieán": "nghịch biến",
    "cöïc trò": "cực trị", "cöïc ñaïi": "cực đại", "cöïc tieåu": "cực tiểu",
    "giaù trò": "giá trị", "lôùn nhaát": "lớn nhất", "nhoû nhaát": "nhỏ nhất",
    "tieäm caän": "tiệm cận", "ñöùng": "đứng", "xieân": "xiên",
    "khoaûng": "khoảng", "ñoaïn": "đoạn", "taäp xaùc ñònh": "tập xác định",
    "dieän tích": "diện tích", "theå tích": "thể tích", "hình phaúng": "hình phẳng",
    "xaùc suaát": "xác suất", "toå hôïp": "tổ hợp",
    "maët phaúng": "mặt phẳng", "ñöôøng thaúng": "đường thẳng", "khoaûng caùch": "khoảng cách",
    "toïa ñoä": "tọa độ", "vectô": "vectơ", "maët caàu": "mặt cầu",
    "tam giaùc": "tam giác", "töù dieän": "tứ diện", "hình choùp": "hình chóp",
    "hình laêng truï": "hình lăng trụ", "hình hoäp": "hình hộp",
    "caáp soá coäng": "cấp số cộng", "caáp soá nhaân": "cấp số nhân",
    "phöông sai": "phương sai", "ñoä leäch chuaån": "độ lệch chuẩn",
    "trung vò": "trung vị", "moát": "mốt", "töù phaân vò": "tứ phân vị",
    "nghieäm": "nghiệm", "coù": "có", "baèng": "bằng", "ñöôïc": "được",
    "ñuùng": "đúng"
}


def clean_mathtype_symbols(text: str) -> str:
    """Lọc và chuẩn hóa các ký hiệu lỗi font MathType, Symbol, VNI sang ký tự toán học chuẩn."""
    if not text:
        return ""

    for vni_k, vni_v in VNI_COMMON_MAP.items():
        if vni_k in text:
            text = text.replace(vni_k, vni_v)

    text = re.sub(r'[\uf0e9\uf0ea\uf0eb]+', '[', text)
    text = re.sub(r'[\uf0f9\uf0fa\uf0fb]+', ']', text)
    text = re.sub(r'[\uf0e6\uf0e7\uf0e8]+', '(', text)
    text = re.sub(r'[\uf0f6\uf0f7\uf0f8]+', ')', text)
    text = re.sub(r'[\uf0ec\uf0ed\uf0ee\uf0ef\uf8f1\uf8f2\uf8f3]+', '{', text)
    text = re.sub(r'[\uf0fc\uf0fd\uf0fe]+', '}', text)

    res = []
    for ch in text:
        code = ord(ch)
        if code in MATHTYPE_SYMBOL_MAP:
            res.append(MATHTYPE_SYMBOL_MAP[code])
        elif 0xf020 <= code <= 0xf07e:
            res.append(chr(code - 0xf000))
        elif 0xf000 <= code <= 0xf8ff:
            res.append(" ")
        else:
            res.append(ch)
    cleaned = "".join(res)

    cleaned = re.sub(r'([\-0-9a-zA-Z\+;\.e\u03c0]+(?:;[\-0-9a-zA-Z\+;\.e\u03c0]+)?)\s*(?:\[\s*\])+', r'[\1]', cleaned)
    cleaned = re.sub(r'\[\s*\n\s*\]', '', cleaned)
    cleaned = re.sub(r'\(\s*\n\s*\)', '', cleaned)
    cleaned = re.sub(r'\{\s*\n\s*\}', '', cleaned)
    cleaned = re.sub(r'^\s*(\[\]|\(\)|\{\})\s*\.?$', '', cleaned, flags=re.MULTILINE)

    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    cleaned = re.sub(r' +([,;:.\)\]])', r'\1', cleaned)
    cleaned = re.sub(r'([\(\[]) +', r'\1', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned
