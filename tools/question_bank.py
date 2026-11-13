# -*- coding: utf-8 -*-
"""Thư viện câu hỏi (ngân hàng câu hỏi) – gom MỌI câu hỏi luyện tập đã từng có trên các trang bài học, kể cả câu đã được thay ra
khi hiệu chỉnh (lấy lại từ lịch sử git), để sau này đổi qua lại giữa các câu cùng dạng.

    python tools/question_bank.py                      # quét các trang hiện tại + phiên bản cũ ở OLD_REF (nếu có kho git)
    python tools/question_bank.py --old-ref <commit>   # chọn mốc phiên bản cũ
    python tools/question_bank.py --git <đường-dẫn-kho>  # kho git chứa lịch sử (mặc định: thư mục dự án)

Kết quả: data/question-bank/grade<lớp>/<mã-bài>.json, mỗi tệp:
  {"lesson": mã, "grade", "no", "title", "items": [câu, ...]}
Mỗi câu: id (băm nội dung), status ("đang dùng" | "đã thay ra"), sources (danh sách mốc), level (1–3), section (A/B/C/D…),
  type (mcq | tf | short), form (khung dạng: đề tiếng Anh đã thay số bằng #, câu cùng form là cùng dạng → đổi được cho nhau),
  en, vi (HTML đề, gồm cả hình/bảng), options (HTML từng phương án, với mcq), answer (chữ cái / true|false / đáp số),
  explain_en, explain_vi (HTML lời giải), images (đường dẫn hình dùng trong câu).
Câu trùng nội dung chỉ lưu một lần; câu đang dùng và câu đã thay ra cùng nằm trong một tệp."""
import os, re, sys, json, hashlib, subprocess, html as _h

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD_REF = '9dde968'          # mốc trước đợt hiệu chỉnh 13/11/2026 (lớp 11 đợt 1–2, lớp 12 đợt 1)

def _strip(t): return _h.unescape(re.sub(r'<[^>]+>', '', t))
def _tx(block):
    """(en, vi) từ một khối <div class="tx">…</div>."""
    en = re.search(r'<(p|div) class="en"[^>]*>(.*?)</\1>(?=<button)', block, re.S)
    vi = re.search(r'<(p|div) class="vi">(.*)</\1>\s*$', block, re.S)
    return (en.group(2) if en else ''), (vi.group(2) if vi else '')

def form_of(en):
    t = _strip(en)
    t = re.sub(r'\\\((.*?)\\\)', lambda m: '\\(' + re.sub(r'\d+(?:[.,]\d+)?', '#', m.group(1)) + '\\)', t)
    t = re.sub(r'\d+(?:[.,]\d+)?', '#', t)
    return re.sub(r'\s+', ' ', t).strip()

def parse_page(h):
    out = []
    marks = [(m.start(), int(m.group(1))) for m in re.finditer(r'lv-only-(\d)"', h)]
    secs = [(m.start(), _strip(m.group(1))) for m in re.finditer(r'<p class="mbl-group"><span class="txi"><span class="en">(.*?)</span>', h)]
    for m in re.finditer(r'<div class="mbl-item" data-type="(\w+)"(?: data-kind="\w+")? data-answer="([^"]*)">(.*?)<div class="mbl-explain" hidden>(.*?)</div></div>(?=</div>)', h, re.S):
        typ, ans, body, ex = m.group(1), _h.unescape(m.group(2)), m.group(3), m.group(4)
        lv = max([x for x in marks if x[0] < m.start()] or [(0, 0)])[1]
        sec = max([x for x in secs if x[0] < m.start()] or [(0, '')])[1]
        q = re.search(r'<div class="tx">(.*?)</div>(?=<div class="(?:mbl-opts|tx)|<p><input)', body, re.S)
        en, vi = _tx(q.group(1)) if q else ('', '')
        opts = re.findall(r'<input type="radio" name="\w+" value="\w+"><span>(.*?)</span></label>', body, re.S) if typ == 'mcq' else []
        een, evi = _tx(ex)
        imgs = sorted(set(re.findall(r'img/[\w-]+/[0-9a-f]+\.(?:svg|png)', en + vi)))
        out.append(dict(level=lv, section=sec.split('.')[0].strip(), type=typ, form=form_of(en), en=en, vi=vi, options=opts, answer=ans,
                        explain_en=een, explain_vi=evi, images=imgs))
    return out

def _norm(t):
    """Chuẩn hóa để nhận ra cùng một câu dù cách trình bày đổi (bảng chỉ giữ số trong ô, dấu thập phân, khoảng trắng, nhãn song ngữ)."""
    t = re.sub(r'<table.*?</table>', lambda m: ' '.join(re.findall(r'<td[^>]*>(.*?)</td>|<th scope="col">(.*?)</th>', m.group(0)) and
               [a or b for a, b in re.findall(r'<td[^>]*>(.*?)</td>|<th scope="col">(.*?)</th>', m.group(0))]), t, flags=re.S)
    t = _strip(t).replace('{,}', '.').replace('\\,', '')
    t = re.sub(r'[^\x00-\x7f]+', ' ', t.replace('Cộng', ' ')).replace('Total', ' ')
    return re.sub(r'\s+', '', t)
def _en_only(o):
    m = re.search(r'<span class="en">(.*?)</span>', o, re.S)
    return m.group(1) if m else o
def _key(q): return hashlib.md5((q['type'] + '|' + _norm(q['en']) + '|' + '|'.join(_norm(_en_only(o)) for o in q['options']) + '|' + q['answer']).encode()).hexdigest()[:12]

def git_show(repo, ref, path):
    try: return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (ref, path)], capture_output=True, text=True, check=True).stdout
    except Exception: return None

def build(old_ref=OLD_REF, repo=ROOT):
    lessons = json.load(open(os.path.join(ROOT, 'lessons.json'), encoding='utf-8'))
    tot = {'đang dùng': 0, 'đã thay ra': 0}
    for L in lessons:
        p = os.path.join(ROOT, L['path'])
        if not os.path.exists(p): continue
        cur = parse_page(open(p, encoding='utf-8').read())
        bank = {}
        for q in cur:
            k = _key(q); q.update(id=k, status='đang dùng', sources=['hiện tại']); bank.setdefault(k, q)
        old = git_show(repo, old_ref, L['path']) if old_ref else None
        if old:
            for q in parse_page(old):
                k = _key(q)
                if k in bank: bank[k]['sources'].append(old_ref); continue
                q.update(id=k, status='đã thay ra', sources=[old_ref]); bank[k] = q
        # giữ các câu đã thay ra từ lần chạy trước (không bao giờ xóa câu khỏi thư viện)
        out = os.path.join(ROOT, 'data', 'question-bank', 'grade%d' % L['grade'], L['id'] + '.json')
        if os.path.exists(out):
            for q in json.load(open(out, encoding='utf-8'))['items']:
                if q['id'] not in bank: q['status'] = 'đã thay ra'; bank[q['id']] = q
        items = sorted(bank.values(), key=lambda q: (q['status'] != 'đang dùng', q['level'], q['section'], q['form']))
        for q in items: tot[q['status']] += 1
        os.makedirs(os.path.dirname(out), exist_ok=True)
        json.dump(dict(lesson=L['id'], grade=L['grade'], no=L.get('no'), title=L['title'], path=L['path'], items=items),
                  open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('Thư viện câu hỏi: %d câu đang dùng, %d câu đã thay ra.' % (tot['đang dùng'], tot['đã thay ra']))

if __name__ == '__main__':
    a = sys.argv[1:]
    ref = a[a.index('--old-ref') + 1] if '--old-ref' in a else OLD_REF
    repo = a[a.index('--git') + 1] if '--git' in a else ROOT
    build(ref, repo)
