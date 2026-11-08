# -*- coding: utf-8 -*-
"""BỘ DỰNG BÀI HỌC DUY NHẤT của MathBridge (dùng cho mọi khối lớp 1-12).

Nguyên tắc: bài học = NỘI DUNG (do người viết nhập, theo từng lớp) + MÔ HÌNH (config/model.json, dùng chung).
  - Nội dung chỉ gồm: tiêu đề, mục tiêu, từ vựng, lý thuyết, ví dụ, bài tập... KHÔNG chứa bố cục, số mục, tên mục, số lớp.
  - Mô hình quyết định: có những mục nào, thứ tự, tên mục (EN/VI), mục nào ẩn ở Mức 1, khung trang, CSS/JS nạp,
    cấp học, và ngoại lệ theo cấp/lớp.
Sửa config/model.json (hoặc css/lesson-kit-v2.*, config/page-template.html) rồi chạy `python tools/build_all.py`
-> mọi bài của mọi lớp được dựng lại.

Lớp được suy ra từ mã bài `g<lớp>-...` (ví dụ g12-mono-01 -> lớp 12), thư mục = lessons/grade<lớp>/<chủ-đề>/<tệp>.html.
"""
import os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mb_lib import *
import mb_lib

REGISTRY = []   # các bài đã dựng trong lần chạy này (dùng cho build_all)


def grade_of(lid):
    m = re.match(r'^g(\d{1,2})-', lid)
    if not m or not 1 <= int(m.group(1)) <= 12:
        raise ValueError('Mã bài phải bắt đầu bằng g<lớp 1-12>-, nhận được: ' + lid)
    return int(m.group(1))


def stage_of(grade):
    for st in model()['stages']:
        if grade in st['grades']:
            return st
    raise ValueError('Lớp %d chưa thuộc cấp học nào trong config/model.json' % grade)


def sections_for(grade):
    """Danh sách mục áp dụng cho một lớp = mô hình chung trừ các mục bị ẩn theo cấp học / theo lớp."""
    m = model()
    hide = set(stage_of(grade).get('hideSections', []))
    hide |= set(m.get('gradeOverrides', {}).get(str(grade), {}).get('hideSections', []))
    return [s for s in m['sections'] if s['key'] not in hide]


# ---------------- Bộ vẽ từng loại mục (type trong model.json) ----------------
def _renumber(html, n):
    """Tiêu đề phụ trong nội dung viết dạng '<h3>5.1 ...' sẽ được đánh số lại theo số mục thật trong mô hình."""
    return re.sub(r'<h3>\d+\.(\d+)(\s)', lambda mo: '<h3>%d.%s%s' % (n, mo.group(1), mo.group(2)), html)


def _r_intro(sec, c, grade, n):
    m = model(); mt = m['meta']
    ti = lambda k: TI(mt[k]['en'], mt[k]['vi'])
    meta = c['meta']
    s = ('<div class="mbl-meta"><div><b>%s</b>%d</div><div><b>%s</b>%s</div><div><b>%s</b>%s</div><div><b>%s</b>%s</div></div>' % (
        ti('grade'), grade, ti('level'), TI(*meta['level']), ti('time'), TI(*meta['time']), ti('before'), TI(*meta['before'])))
    gt, gl = sec['goalsTitle'], sec['goalsLead']
    s += BOX('blue', (gt['en'], gt['vi']), T(gl['en'], gl['vi']), UL([T(*g) for g in c['goals']]))
    return s


def _r_vocab(sec, c, grade, n):
    return UL([VOC(*v) for v in c['vocab']])


def _r_phrases(sec, c, grade, n):
    return UL([T(*p) for p in c['phrases']])


def _r_html(sec, c, grade, n):
    return _renumber(c[sec['key']], n)


def _r_quiz(sec, c, grade, n):
    return QUIZ(c[sec['key']])


def _r_mistakes(sec, c, grade, n):
    return BOX('yellow', None, UL([T(*x) for x in c[sec['key']]]))


def _r_bullets(sec, c, grade, n):
    return UL([T(*x) for x in c[sec['key']]])


def _r_checks(sec, c, grade, n):
    return CHECKS(c[sec['key']])


RENDERERS = {'intro': _r_intro, 'vocab': _r_vocab, 'phrases': _r_phrases, 'html': _r_html, 'quiz': _r_quiz,
             'mistakes': _r_mistakes, 'bullets': _r_bullets, 'checks': _r_checks}


def has_content(sec, c):
    k = sec['key']
    if sec['type'] == 'intro':
        return bool(c.get('meta')) and bool(c.get('goals'))
    return bool(c.get(k))


# ---------------- Dựng một bài ----------------
def render(c):
    """c: dict nội dung bài. Trả về (html, entry). Không ghi file."""
    lid = c['id']; grade = grade_of(lid)
    m = model(); pg = m['page']
    topic_en, topic_vi = c['topic']
    reset(); set_title(lid, c['title_en'], c['title_vi'])
    body, toc, n = '', [], 0
    for sec in sections_for(grade):
        if not has_content(sec, c):
            if sec.get('required'):
                raise ValueError('Bài %s thiếu mục bắt buộc "%s" (%s)' % (lid, sec['key'], sec['en']))
            continue
        n += 1
        part = H2(n, sec['en'], sec['vi']) + RENDERERS[sec['type']](sec, c, grade, n)
        cls = level_class(sec.get('levels'))
        body += '<div class="%s">%s</div>' % (cls, part) if cls else part
        toc.append((n, sec['toc'][0], sec['toc'][1], sec.get('levels')))
    sub = TI(pg['subtitle']['en'].format(grade=grade, topic_en=topic_en),
             pg['subtitle']['vi'].format(grade=grade, topic_vi=topic_vi))
    path = c.get('path') or 'lessons/grade%d/%s/%s.html' % (grade, c['folder'], c['file'])
    depth = path.count('/')
    html = PAGE(lid, c['title_en'], depth, sub, '', body, toc)
    entry = {'id': lid, 'grade': grade, 'category': topic_en, 'title': c['title_en'], 'description': c['description'],
             'level': c['level'], 'estimatedMinutes': c['minutes'], 'prerequisites': c.get('prerequisites', []),
             'path': path, 'tags': c.get('tags', [])}
    cat = model().get('catalog', {})
    if cat.get('language') == 'vi':      # lessons.json hiển thị bằng tiếng Việt (xem "catalog" trong model.json)
        old_cat = _legacy_catalog().get(lid)
        entry['title'] = c.get('catalog_title_vi') or (old_cat[0] if old_cat else c['title_vi'])
        entry['category'] = cat.get('categoryVi', {}).get(topic_en, topic_vi)
        entry['description'] = c.get('description_vi') or (old_cat[1] if old_cat else c['description'])
        entry['tags'] = list(c.get('tags_vi') or (old_cat[2] if old_cat else c.get('tags', [])))
    return html, entry


_legacy = []
def _legacy_catalog():
    """content/catalog-vi.json: tiêu đề/mô tả/từ khóa tiếng Việt của các bài viết trước khi có description_vi, tags_vi."""
    if not _legacy:
        p = os.path.join(ROOT, 'content', 'catalog-vi.json')
        _legacy.append(json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {})
    return _legacy[0]


def fix_math_lt(html):
    """Dấu < thô trong công thức \\( … \\) bị trình duyệt hiểu là thẻ HTML và làm mất công thức: đổi thành \\lt ."""
    segs = re.split(r'(<script.*?</script>)', html, flags=re.S)
    f = lambda m: m.group(0).replace('<', '\\lt ')
    return ''.join(x if i % 2 else re.sub(r'(?<!\\)\\\((?:(?!\\\)).)*?\\\)', f, x, flags=re.S) for i, x in enumerate(segs))


def fix_math_prime(html):
    """Trong công thức \\( … \\) / \\[ … \\], ký tự ′ (U+2032) bị MathJax vẽ ở chân chữ (A′ thành "Aı").
    Đổi sang dấu nháy ' để TeX dựng dấu phẩy trên chuẩn SGK: A'B'C'D', f'(x). Chữ thường và nhãn hình vẽ giữ nguyên ′."""
    segs = re.split(r'(<script.*?</script>)', html, flags=re.S)
    f = lambda m: m.group(0).replace('″', "''").replace('′', "'")
    pat = r'(?<!\\)\\\((?:(?!\\\)).)*?\\\)|(?<!\\)\\\[(?:(?!\\\]).)*?\\\]'
    return ''.join(x if i % 2 else re.sub(pat, f, x, flags=re.S) for i, x in enumerate(segs))


_MATH_SEG = r'(?<!\\)\\\((?:(?!\\\)).)*?\\\)|(?<!\\)\\\[(?:(?!\\\]).)*?\\\]'

def _dfrac_math(s):
    """Trong một công thức: \\frac -> \\dfrac và a/b (số) -> \\dfrac{a}{b}, TRỪ khi nằm trong số mũ/chỉ số (^, _)
    – ở đó giữ \\frac và dấu / cho gọn (ví dụ \\(2^{t/20}\\), \\(\\big|_0^{\\pi/2}\\), \\(16^{-\\frac34}\\))."""
    out = []; stack = []; i = 0; n = len(s); after_script = False
    while i < n:
        ch = s[i]
        if ch == '\\' and s.startswith('\\frac', i) and not s[i + 5:i + 6].isalpha():
            out.append('\\frac' if (after_script or any(stack)) else '\\dfrac'); i += 5; after_script = False; continue
        if ch == '\\' and i + 1 < n:            # lệnh khác: chép nguyên tên lệnh
            j = i + 1
            while j < n and s[j].isalpha(): j += 1
            if j == i + 1: j += 1
            out.append(s[i:j]); i = j; after_script = False; continue
        if ch == '{':
            stack.append(after_script or any(stack)); after_script = False; out.append(ch); i += 1; continue
        if ch == '}':
            if stack: stack.pop()
            out.append(ch); i += 1; continue
        if ch in '^_':
            after_script = True; out.append(ch); i += 1; continue
        if ch.isdigit() and not (after_script or any(stack)) and (i == 0 or not (s[i - 1].isalnum() or s[i - 1] in '.,' or s[max(0, i - 3):i] == '{,}')):
            m = re.match(r'(\d+)/(\d+)(?![\d.,])', s[i:])
            if m:
                out.append('\\dfrac{%s}{%s}' % m.groups()); i += m.end(); continue
        if not ch.isspace(): after_script = False
        out.append(ch); i += 1
    return ''.join(out)

_ENUM_LET = re.compile(r'(?<![\w(\[])\(?([a-h])\)(?=\s)')       # a) b) … hoặc (a) (b) …
_ENUM_NUM = re.compile(r'(?<![\w(\[])\((\d)\)(?=\s)')

def _enum_breaks(content):
    """Trong một đoạn văn: các ý a) b) c)… hoặc (1) (2)… viết liền một dòng thì mỗi ý xuống dòng (góp ý 08/11/2026).
    Chỉ xét chữ ngoài công thức và ngoài thẻ; cần có ít nhất hai ý liên tiếp (a và b, hoặc 1 và 2)."""
    parts = re.split('(' + _MATH_SEG + r'|<[^>]+>)', content, flags=re.S)
    flat = ''.join(p if i % 2 == 0 else ('\x00' if p.startswith('<') else 'X') for i, p in enumerate(parts))   # vị trí để xét ký tự đứng trước
    def marks(rx, first, second, strict):
        found = []; want = first                       # các ý phải đi đúng thứ tự a, b, c… (hoặc 1, 2, 3…)
        for m in rx.finditer(flat):
            if m.group(1) != want: continue
            prev = flat[:m.start()].rstrip(' \t\n\x00')
            ok_prev = (not prev) or prev[-1] in ':;.?,' or (not strict and m.group(1) == first)
            if ok_prev: found.append((m.start(), m.group(1))); want = chr(ord(want) + 1)
        return found if len(found) >= 2 else []
    pos = marks(_ENUM_LET, 'a', 'b', False) + marks(_ENUM_NUM, '1', '2', True)
    if not pos: return content
    ins = set(p for p, _ in pos if flat[:p].strip(' \t\n\x00'))
    # ánh xạ vị trí trong flat về chuỗi gốc
    out = []; k = 0
    for i, p in enumerate(parts):
        if i % 2 == 0:
            for j, ch in enumerate(p):
                if k + j in ins:
                    while out and out[-1] in (' ', '\t', '\n'): out.pop()
                    if not (out and re.fullmatch(r'<br\s*/?>', out[-1])): out.append('<br>')
                out.append(ch)
            k += len(p)
        else:
            out.append(p); k += 1
    return ''.join(out)

def fix_layout(html):
    """Hậu xử lý trình bày (góp ý của chủ website 08/11/2026): phân số \\dfrac; các ý a) b)/(1) (2) xuống dòng;
    câu hỏi '…?' kèm danh sách liệt kê thì danh sách xuống dòng dưới câu hỏi."""
    segs = re.split(r'(<script.*?</script>|<style.*?</style>)', html, flags=re.S)
    def body(x):
        x = re.sub(_MATH_SEG, lambda m: _dfrac_math(m.group(0)), x, flags=re.S)
        x = re.sub(r'(<(p|li)(?:\s[^>]*)?>)(.*?)(</\2>)', lambda m: m.group(1) + _enum_breaks(m.group(3)) + m.group(4), x, flags=re.S)
        x = re.sub(r'\?\s+(?=\\\((?:(?!\\\)).)*?\\\)\s*[,;]\s*\\\()', '?<br>', x)
        return x
    return ''.join(x if i % 2 else body(x) for i, x in enumerate(segs))


def lesson(**c):
    """Điểm nhập duy nhất của người viết nội dung. Dựng bài, ghi file; lessons.json do build_all tổng hợp."""
    html, entry = render(c)
    html = fix_layout(fix_math_prime(fix_math_lt(html)))
    out = os.path.join(ROOT, entry['path']); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(html)
    REGISTRY.append((c.get('order', 0), entry))
    print('written', entry['path'], len(html))
    return entry


def sync_lessons_json():
    """Gộp các bài vừa dựng vào lessons.json. Bài chưa chuyển sang mô hình (bản mẫu cũ) được giữ nguyên.
    Thứ tự trong cùng một lớp: các bài đã viết theo mô hình xếp theo `order` (rồi theo thứ tự dựng), bài mẫu cũ chưa chuyển đứng sau."""
    p = os.path.join(ROOT, 'lessons.json')
    with open(p, encoding='utf-8') as fh: old = json.load(fh)
    lo = {k: v for k, v in (model().get('lessonOrder') or {}).items() if not k.startswith('_')}
    built = {e['id']: (lo.get(e['id'], o), i, e) for i, (o, e) in enumerate(REGISTRY)}
    keep = [(lo.get(x['id'], 1000), -1, x) for x in old if x['id'] not in built]   # bài mẫu cũ chưa chuyển: đứng sau các bài đã viết theo mô hình
    allx = [((e['grade'], o, i), e) for (o, i, e) in built.values()] + [((x['grade'], o_, k), x) for k, (o_, _, x) in enumerate(keep)]
    allx.sort(key=lambda t: t[0])
    res = [e for _, e in allx]
    nos = {k: v for k, v in (model().get('lessonNo') or {}).items() if not k.startswith('_')}
    locked = {k: v for k, v in (model().get('lockedLessons') or {}).items() if not k.startswith('_')}
    for e in res:                          # tạm khóa theo config/model.json (lockedLessons)
        e.pop('locked', None); e.pop('lockNote', None); e.pop('no', None)
        if e['id'] in nos: e['no'] = nos[e['id']]
        if e['id'] in locked: e['locked'] = True; e['lockNote'] = locked[e['id']]
    ids = [e['id'] for e in res]
    assert len(ids) == len(set(ids)), 'id bài học bị trùng'
    with open(p, 'w', encoding='utf-8') as fh: json.dump(res, fh, ensure_ascii=False, indent=2)
    cmap = model().get('catalog', {}).get('categoryVi')
    if cmap:                              # chủ đề trong từ vựng cũng hiển thị bằng tiếng Việt
        vp = os.path.join(ROOT, 'data', 'vocab.json')
        with open(vp, encoding='utf-8') as fh: v = json.load(fh)
        for x in v: x['category'] = cmap.get(x['category'], x['category'])
        with open(vp, 'w', encoding='utf-8') as fh: json.dump(v, fh, ensure_ascii=False, indent=2)
    return res


def check_model():
    """Kiểm tra mô hình: khóa mục không trùng, type hợp lệ, mỗi lớp 1-12 thuộc đúng một cấp học."""
    m = model(); keys = [s['key'] for s in m['sections']]
    assert len(keys) == len(set(keys)), 'khóa mục bị trùng trong model.json'
    for s in m['sections']:
        assert s['type'] in RENDERERS, 'type mục không hợp lệ: ' + s['type']
    gs = [g for st in m['stages'] for g in st['grades']]
    assert sorted(gs) == list(range(1, 13)), 'các cấp học phải phủ đúng lớp 1-12, mỗi lớp một lần'
    return True
