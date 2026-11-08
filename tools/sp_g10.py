# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 1 (mệnh đề), Bài 2 (tập hợp), Bài 3 (bất phương trình bậc nhất hai ẩn).
Mọi đáp án được tính bằng máy (duyệt miền mẫu) và đối chiếu với công thức."""
import math
from fractions import Fraction as F
from mb_selfpractice import *

RS = [F(i, 2) for i in range(-60, 61)]; ZS = list(range(-40, 41)); NS = list(range(0, 61)); NP = list(range(1, 61))
def _forall(dom, p): return all(p(x) for x in dom)
def _exists(dom, p): return any(p(x) for x in dom)
DOMTEX = {'R': ('\\mathbb{R}', RS), 'Z': ('\\mathbb{Z}', ZS), 'N': ('\\mathbb{N}', NS), 'P': ('\\mathbb{N}^*', NP)}

# ---------- Bài 1: mệnh đề ----------
def _stmt(r):
    """Sinh một mệnh đề có lượng từ, trả về (tex, true?)."""
    t = r.choice(range(6))
    if t == 0:
        a = r.randint(-3, 5); b = r.randint(-3, 5); tex = '\\forall x\\in\\mathbb{R},\\ x^2%s>%d' % (('%+d' % a) if a else '', b); val = _forall(RS, lambda x: x * x + a > b); assert val == (a > b)
    elif t == 1:
        k = r.randint(-9, 16); tex = '\\exists x\\in\\mathbb{R},\\ x^2=%d' % k; val = _exists(RS + [F(i, 1) for i in range(-60, 61)], lambda x: x * x == k) if k >= 0 and k <= 16 else False
        val = (k >= 0 and any(i * i == k for i in range(0, 5)) or (k >= 0 and k <= 16 and any(F(i, 2) ** 2 == k for i in range(0, 9)))); val = (k >= 0)  # x=sqrt(k) tồn tại trong R
    elif t == 2:
        k = r.randint(1, 4); tex = '\\forall n\\in\\mathbb{N}^*,\\ n^2\\ge %dn' % k; val = _forall(NP, lambda n: n * n >= k * n); assert val == (k <= 1)
    elif t == 3:
        m = r.randint(2, 40); tex = '\\exists n\\in\\mathbb{N},\\ n^2=%d' % m; val = _exists(NS, lambda n: n * n == m)
    elif t == 4:
        k = r.randint(1, 15); tex = '\\exists x\\in\\mathbb{Z},\\ 2x=%d' % k; val = _exists(ZS, lambda x: 2 * x == k); assert val == (k % 2 == 0)
    else:
        a = r.randint(2, 6); tex = '\\forall x\\in\\mathbb{R},\\ x^2\\ge %dx' % a; val = _forall(RS, lambda x: x * x >= a * x)   # sai (x = a/2)
        assert not val
    return tex, val

def _stem(r, pool): return r.choice(pool)
ST_TRUE = [('Which of these statements is true?', 'Phát biểu nào sau đây là đúng?'), ('Which statement below is true?', 'Phát biểu nào dưới đây đúng?'), ('Pick the true statement.', 'Chọn phát biểu đúng.'),
           ('Exactly one statement is true. Which one?', 'Chỉ có một phát biểu đúng. Đó là phát biểu nào?'), ('Which of the following is a true statement?', 'Trong các phát biểu sau, phát biểu nào là mệnh đề đúng?'), ('Choose the true proposition.', 'Hãy chọn mệnh đề đúng.')]
ST_PROP = [('Which of these is a proposition (it is true or false)?', 'Câu nào sau đây là một mệnh đề (đúng hoặc sai)?'), ('Choose the proposition.', 'Chọn mệnh đề.'), ('Exactly one of these is a proposition. Which one?', 'Chỉ có một câu là mệnh đề. Đó là câu nào?'), ('Which option is a proposition?', 'Phương án nào là một mệnh đề?')]
ST_IMPL = [('Which implication is true for every positive integer \\(n\\)?', 'Mệnh đề kéo theo nào đúng với mọi số nguyên dương \\(n\\)?'), ('Choose the implication that is always true for positive integers \\(n\\).', 'Chọn mệnh đề kéo theo luôn đúng với số nguyên dương \\(n\\).'), ('Only one implication is true for all positive integers \\(n\\). Which one?', 'Chỉ một mệnh đề kéo theo đúng với mọi số nguyên dương \\(n\\). Đó là mệnh đề nào?'), ('Which of these implications has no counterexample?', 'Mệnh đề kéo theo nào sau đây không có phản ví dụ?')]
ST_EQ = [('Which equivalence is true for every real number \\(x\\)?', 'Mệnh đề tương đương nào đúng với mọi số thực \\(x\\)?'), ('Choose the equivalence that holds for all real \\(x\\).', 'Chọn mệnh đề tương đương đúng với mọi số thực \\(x\\).'), ('Only one equivalence is true for all real \\(x\\). Which one?', 'Chỉ một mệnh đề tương đương đúng với mọi số thực \\(x\\). Đó là câu nào?'), ('Which \\(\\Leftrightarrow\\) statement is always true?', 'Mệnh đề \\(\\Leftrightarrow\\) nào luôn đúng?')]

def p_true(r, lv):
    while True:
        items = [_stmt(r) for _ in range(4)]
        if len({t for t, _ in items}) == 4 and sum(v for _, v in items) == 1: break
    ans = [v for _, v in items].index(True)
    sq = _stem(r, ST_TRUE)
    return dict(en=sq[0], vi=sq[1], opts=[t for t, _ in items], ans=ans,
      ee='Check each statement: only the chosen one is true; for the others find a counterexample or show that no such number exists.', ev='Kiểm tra từng phát biểu: chỉ phát biểu được chọn là đúng; với các phát biểu còn lại hãy chỉ ra phản ví dụ hoặc chứng tỏ không có số nào thỏa mãn.')

def p_count(r, lv):
    while True:
        items = [_stmt(r) for _ in range(4)]
        if len({t for t, _ in items}) == 4 and 1 <= sum(v for _, v in items) <= 3: break
    c = sum(v for _, v in items); st = '; '.join('(%d)\\ %s' % (i + 1, t) for i, (t, _) in enumerate(items))
    others = [x for x in range(0, 5) if x != c]; r.shuffle(others)
    return dict(en='How many of these four statements are true? %s' % ('\\(' + st + '\\)'), vi='Trong bốn phát biểu sau có bao nhiêu phát biểu đúng? %s' % ('\\(' + st + '\\)'),
      opts=[str(c)] + [str(x) for x in others[:3]], ans=0, ee='Decide each statement separately: %d of them are true.' % c, ev='Xét từng phát biểu: có %d phát biểu đúng.' % c)

PROPS = ['2^{10}=1024', '(-3)^2=-9', '\\sqrt{16}=4', '5-8>0', '7\\times8=56', '\\dfrac{1}{2}+\\dfrac{1}{3}=\\dfrac{2}{5}', '10^2<99', '3^3=27', '(-2)^3>0', '9-4=5']
OPENS = ['x+3=7', 'y^2<9', 'n-4>1', '2a=b', 'x^2-1=0', 'm\\ge5', 'x+y=10', 'k^2=2k', 't\\le-1', '3z>12']
def p_prop(r, lv):
    c = r.choice(PROPS); o = r.sample(OPENS, 3)
    sq = _stem(r, ST_PROP)
    return dict(en=sq[0], vi=sq[1], opts=[c] + o, ans=0,
      ee='\\(%s\\) has no variable, so it is true or false. The others contain a variable: their truth depends on its value.' % c, ev='\\(%s\\) không chứa biến nên chắc chắn đúng hoặc sai. Các câu còn lại chứa biến: tính đúng sai phụ thuộc giá trị của biến.' % c)

def p_neg(r, lv):
    q = r.choice(['A', 'E']); dom = r.choice(['R', 'Z', 'N']); v = 'x' if dom != 'N' else 'n'; rel = r.choice(['>', '\\ge', '<', '\\le']); k = r.randint(0, 9)
    flip = {'>': '\\le', '\\ge': '<', '<': '\\ge', '\\le': '>'}; sq = {'A': '\\forall', 'E': '\\exists'}; other = {'A': 'E', 'E': 'A'}
    dtex = DOMTEX[dom][0]
    s = lambda qq, rr: '%s %s\\in%s,\\ %s^2%s %d' % (sq[qq], v, dtex, v, rr, k) if False else '%s %s\\in%s,\\ %s%s%d' % (sq[qq], v, dtex, v, rr, k)
    cor = s(other[q], flip[rel]); wrong = [s(q, flip[rel]), s(other[q], rel), s(q, rel)]
    return dict(en='Write the negation of \\(%s\\).' % s(q, rel), vi='Phủ định của mệnh đề \\(%s\\) là mệnh đề nào?' % s(q, rel), opts=[cor] + wrong, ans=0,
      ee='Swap \\(\\forall\\) and \\(\\exists\\), and negate the inequality: \\(%s\\).' % cor, ev='Đổi \\(\\forall\\) thành \\(\\exists\\) (và ngược lại) rồi phủ định bất đẳng thức: \\(%s\\).' % cor)

def p_impl(r, lv):
    while True:
        pairs = [(r.choice([2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18]), r.choice([2, 3, 4, 5, 6, 9, 10, 12])) for _ in range(4)]
        pairs = [(a, b) for a, b in pairs if a != b]
        if len(pairs) == 4 and len(set(pairs)) == 4 and sum(a % b == 0 for a, b in pairs) == 1: break
    for a, b in pairs:
        holds = _forall(range(1, 400), lambda n: (n % a != 0) or (n % b == 0)); assert holds == (a % b == 0)
    ans = [a % b == 0 for a, b in pairs].index(True); a0, b0 = pairs[ans]
    sq = _stem(r, ST_IMPL)
    return dict(en=sq[0], vi=sq[1], opts=['%d\\mid n\\Rightarrow %d\\mid n' % (a, b) for a, b in pairs], ans=ans,
      ee='\\(%d\\mid n\\Rightarrow %d\\mid n\\) is true because \\(%d\\) is a multiple of \\(%d\\). In the other options find a counterexample.' % (a0, b0, a0, b0), ev='\\(%d\\mid n\\Rightarrow %d\\mid n\\) đúng vì \\(%d\\) là bội của \\(%d\\). Ở các phương án còn lại hãy tìm phản ví dụ.' % (a0, b0, a0, b0))

def p_equiv(r, lv):
    a = r.randint(1, 7); b = r.randint(2, 9); k = r.randint(2, 6)
    good = [('x%+d=%d\\Leftrightarrow x=%d' % (a, b, b - a), lambda x: (x + a == b) == (x == b - a)),
            ('%dx>%d\\Leftrightarrow x>%s' % (k, b, fr(F(b, k))), lambda x: (k * x > b) == (x > F(b, k))),
            ('x^2=%d\\Leftrightarrow |x|=%d' % (k * k, k), lambda x: (x * x == k * k) == (abs(x) == k))]
    bad = [('x^2=%d\\Leftrightarrow x=%d' % (k * k, k), lambda x: (x * x == k * k) == (x == k)),
           ('x^2>%d\\Leftrightarrow x>%d' % (k * k, k), lambda x: (x * x > k * k) == (x > k)),
           ('|x|<%d\\Leftrightarrow x<%d' % (k, k), lambda x: (abs(x) < k) == (x < k)),
           ('x(x-%d)=0\\Leftrightarrow x=%d' % (k, k), lambda x: (x * (x - k) == 0) == (x == k))]
    c = r.choice(good); w = r.sample(bad, 3)
    assert _forall(RS, c[1]) and not any(_forall(RS, f) for _, f in w)
    sq = _stem(r, ST_EQ)
    return dict(en=sq[0], vi=sq[1], opts=[c[0]] + [t for t, _ in w], ans=0,
      ee='The chosen equivalence holds for all real \\(x\\); each other option fails for some \\(x\\) (for example a negative value).', ev='Mệnh đề tương đương được chọn đúng với mọi số thực \\(x\\); mỗi phương án còn lại sai với một giá trị \\(x\\) nào đó (chẳng hạn một số âm).')

B1 = [p_prop, p_true, p_neg, p_impl, p_equiv, p_count, p_neg, p_true]

# ---------- Bài 2: tập hợp ----------
def st(s): return '\\{%s\\}' % ','.join(str(x) for x in sorted(s)) if s else '\\varnothing'
def s_op(r, lv):
    U = range(1, 8 + 3 * lv); A = set(r.sample(list(U), r.randint(4, 6))); B = set(r.sample(list(U), r.randint(4, 6))); op = r.choice(['\\cap', '\\cup', '\\setminus'])
    res = {'\\cap': A & B, '\\cup': A | B, '\\setminus': A - B}[op]
    if not res or res == A or res == B: raise AssertionError
    others = [A & B, A | B, A - B, B - A, A ^ B]
    nm = {'\\cap': ('intersection', 'giao'), '\\cup': ('union', 'hợp'), '\\setminus': ('difference', 'hiệu')}[op]
    return dict(en='Let \\(A=%s\\) and \\(B=%s\\). Find \\(A%s B\\).' % (st(A), st(B), op), vi='Cho \\(A=%s\\), \\(B=%s\\). Tìm \\(A%s B\\).' % (st(A), st(B), op),
      opts=pick_opts(r, st(res), [st(o) for o in others if o != res and o]), ans=0, ee='The %s: \\(A%s B=%s\\).' % (nm[0], op, st(res)), ev='Phép %s: \\(A%s B=%s\\).' % (nm[1], op, st(res)))

def s_subsets(r, lv):
    a = r.randint(-3, 0); b = a + r.randint(3, 3 + lv); S = [x for x in range(a, b)]; n = len(S); kind = r.choice(['all', 'proper'])
    val = 2 ** n if kind == 'all' else 2 ** n - 1
    opts = pick_opts(r, str(val), [str(2 ** n - 1 if kind == 'all' else 2 ** n), str(2 * n), str(n * n), str(2 ** n - 2 if kind == 'proper' else 2 ** (n - 1))])
    return dict(en='How many %ssubsets does \\(\\{x\\in\\mathbb{Z}\\mid %d\\le x<%d\\}\\) have?' % ('' if kind == 'all' else 'proper ', a, b), vi='Tập \\(\\{x\\in\\mathbb{Z}\\mid %d\\le x<%d\\}\\) có bao nhiêu tập con%s?' % (a, b, '' if kind == 'all' else ' thực sự'),
      opts=opts, ans=0, ee='The set has %d elements, so it has \\(2^{%d}=%d\\) subsets%s.' % (n, n, 2 ** n, '' if kind == 'all' else ' (%d proper subsets, without the set itself)' % val),
      ev='Tập có %d phần tử nên có \\(2^{%d}=%d\\) tập con%s.' % (n, n, 2 ** n, '' if kind == 'all' else ' (%d tập con thực sự, trừ chính nó)' % val))

def _iv(a, ac, b, bc): return '%s%d,%d%s' % ('[' if ac else '(', a, b, ']' if bc else ')')
def _inI(x, I): a, ac, b, bc = I; return (x > a or (ac and x == a)) and (x < b or (bc and x == b))
def s_interval(r, lv):
    while True:
        a = r.randint(-6, 0); c = a + r.randint(1, 3); b = c + r.randint(1, 3); d = b + r.randint(1, 3)
        ac, bc, cc, dc = [r.random() < .5 for _ in range(4)]; break
    A = (a, ac, b, bc); B = (c, cc, d, dc); op = r.choice(['\\cap', '\\cup', '\\setminus'])
    grid = [F(i, 2) for i in range(2 * (a - 2), 2 * (d + 2) + 1)]
    if op == '\\cap':
        lo = (c, cc); hi = (b, bc); R = (c, cc, b, bc)
    elif op == '\\cup':
        R = (a, ac, d, dc)
    else:
        R = (a, ac, c, not cc)
    f = {'\\cap': lambda x: _inI(x, A) and _inI(x, B), '\\cup': lambda x: _inI(x, A) or _inI(x, B), '\\setminus': lambda x: _inI(x, A) and not _inI(x, B)}[op]
    assert all(f(x) == _inI(x, R) for x in grid), (A, B, op)
    flip = lambda I, i: tuple((not v) if j == i else v for j, v in enumerate(I))
    others = [flip(R, 1), flip(R, 3), flip(flip(R, 1), 3), (R[0], R[1], B[2], B[3]) if op != '\\cup' else (c, cc, d, dc)]
    return dict(en='Let \\(A=%s\\) and \\(B=%s\\). Find \\(A%s B\\).' % (_iv(*A), _iv(*B), op), vi='Cho \\(A=%s\\), \\(B=%s\\). Tìm \\(A%s B\\).' % (_iv(*A), _iv(*B), op),
      opts=pick_opts(r, _iv(*R), [_iv(*o) for o in others]), ans=0, ee='Draw both intervals on a number line and check each endpoint: \\(A%s B=%s\\).' % (op, _iv(*R)), ev='Vẽ hai khoảng trên trục số và xét từng đầu mút: \\(A%s B=%s\\).' % (op, _iv(*R)))

def s_venn(r, lv):
    p = r.randint(12, 30); q = r.randint(10, 28); k = r.randint(3, min(p, q) - 3); N = p + q - k + r.randint(2, 10); kind = r.choice(['neither', 'only', 'union'])
    val = {'neither': N - (p + q - k), 'only': p - k, 'union': p + q - k}[kind]
    ask = {'neither': ('How many students like neither subject?', 'Có bao nhiêu em không thích môn nào?'), 'only': ('How many students like Math only?', 'Có bao nhiêu em chỉ thích Toán?'), 'union': ('How many students like at least one subject?', 'Có bao nhiêu em thích ít nhất một môn?')}[kind]
    others = [p + q, p + q - k + 1, p - k + 1, N - p - q, q - k, N - (p + q - k) + 2]
    return dict(en='In a class of %d students, %d like Math, %d like English and %d like both. %s' % (N, p, q, k, ask[0]), vi='Một lớp có %d học sinh, %d em thích Toán, %d em thích Tiếng Anh và %d em thích cả hai. %s' % (N, p, q, k, ask[1]),
      opts=pick_opts(r, str(val), [str(o) for o in others if o != val and o > 0]), ans=0,
      ee='\\(n(M\\cup E)=%d+%d-%d=%d\\); %s' % (p, q, k, p + q - k, {'neither': 'so %d-%d=%d like neither.' % (N, p + q - k, val), 'only': 'Math only: %d-%d=%d.' % (p, k, val), 'union': 'this is the answer.'}[kind]),
      ev='\\(n(M\\cup E)=%d+%d-%d=%d\\); %s' % (p, q, k, p + q - k, {'neither': 'nên %d-%d=%d em không thích môn nào.' % (N, p + q - k, val), 'only': 'chỉ thích Toán: %d-%d=%d.' % (p, k, val), 'union': 'đó chính là đáp số.'}[kind]))

def s_comp(r, lv):
    a = r.randint(-5, 3); b = a + r.randint(2, 6); ac, bc = r.random() < .5, r.random() < .5
    I = (a, ac, b, bc); cp = lambda a_, ac_, b_, bc_: '(-\\infty,%d%s\\cup%s%d,+\\infty)' % (a_, ')' if not ac_ else ']', '(' if not bc_ else '[', b_)
    gr = [F(i, 2) for i in range(2 * (a - 3), 2 * (b + 3) + 1)]
    true = (a, not ac, b, not bc)      # phần bù: đầu mút a được lấy khi a không thuộc I
    assert all((not _inI(x, I)) == ((x < a or (not ac and x == a)) or (x > b or (not bc and x == b))) for x in gr)
    # Kiểm định 08/11/2026 (M-001): phương án đúng phải là phần bù thật, tức đảo tính đóng/mở ở mỗi đầu mút.
    # Trước đây phương án đúng là cp(a, ac, b, bc) (giữ nguyên đầu mút như khoảng gốc) – sai.
    inC = lambda x, fa, fb: x < a or (fa and x == a) or x > b or (fb and x == b)
    assert all(inC(x, *true[1::2]) == (not _inI(x, I)) for x in gr)          # phương án đúng = phần bù
    opts = [cp(*true)] + [cp(a, ac, b, bc), cp(a, not ac, b, bc), cp(a, ac, b, not bc)]
    assert all(any(inC(x, fa, fb) != (not _inI(x, I)) for x in gr) for fa, fb in [(ac, bc), (not ac, bc), (ac, not bc)])  # nhiễu đều sai
    return dict(en='Find the complement of \\(%s\\) in \\(\\mathbb{R}\\).' % _iv(*I), vi='Tìm phần bù của \\(%s\\) trong \\(\\mathbb{R}\\).' % _iv(*I), opts=opts, ans=0,
      ee='The complement is everything outside the interval; an endpoint belongs to the complement exactly when it does not belong to the interval: \\(%s\\).' % cp(*true),
      ev='Phần bù gồm mọi số nằm ngoài khoảng; một đầu mút thuộc phần bù đúng khi nó không thuộc khoảng đã cho: \\(%s\\).' % cp(*true)) | {}

def s_count(r, lv):
    k = r.randint(5, 30); t = r.choice(['<', '\\le']); n = sum(1 for x in range(-10, 11) if (x * x < k if t == '<' else x * x <= k))
    others = [n - 1, n + 1, n + 2, n - 2, 2 * n]
    return dict(en='How many elements does \\(\\{x\\in\\mathbb{Z}\\mid x^2%s%d\\}\\) have?' % (t, k), vi='Tập \\(\\{x\\in\\mathbb{Z}\\mid x^2%s%d\\}\\) có bao nhiêu phần tử?' % (t, k),
      opts=pick_opts(r, str(n), [str(o) for o in others if o > 0 and o != n]), ans=0, ee='We need \\(|x|%s\\sqrt{%d}\\): there are %d integers.' % (t, k, n), ev='Cần \\(|x|%s\\sqrt{%d}\\): có %d số nguyên.' % (t, k, n))

B2 = [s_op, s_subsets, s_interval, s_venn, s_comp, s_count, s_interval, s_op]

# ---------- Bài 3: bất phương trình bậc nhất hai ẩn ----------
OPS = {'\\le': lambda v, c: v <= c, '\\ge': lambda v, c: v >= c, '<': lambda v, c: v < c, '>': lambda v, c: v > c}
def ineq(a, b, op, c): return '%s%s%s' % (lin(a, 0, 'x') + ('%+dy' % b if b not in (1, -1) else ('+y' if b == 1 else '-y')) if a else lin(b, 0, 'y'), op, c)
def pt(x, y): return '(%d;%d)' % (x, y)
def i_point(r, lv):
    while True:
        a = r.choice([1, 2, 3, -1, -2]); b = r.choice([1, 2, -1, -3]); c = r.randint(-4, 8); op = r.choice(list(OPS))
        pts = [(r.randint(-4, 5), r.randint(-4, 5)) for _ in range(4)]
        if len(set(pts)) == 4 and sum(OPS[op](a * x + b * y, c) for x, y in pts) == 1: break
    ans = [OPS[op](a * x + b * y, c) for x, y in pts].index(True); x0, y0 = pts[ans]
    return dict(en='Which pair \\((x;y)\\) is a solution of \\(%s\\)?' % ineq(a, b, op, c), vi='Cặp số \\((x;y)\\) nào là nghiệm của bất phương trình \\(%s\\)?' % ineq(a, b, op, c), opts=[pt(*p) for p in pts], ans=ans,
      ee='Substitute: \\(%d\\cdot%d%+d\\cdot%d=%d\\), and \\(%d%s%d\\) is true. The other pairs make it false.' % (a, x0, b, y0, a * x0 + b * y0, a * x0 + b * y0, op, c), ev='Thay vào: \\(%d\\cdot%d%+d\\cdot%d=%d\\) và \\(%d%s%d\\) đúng. Các cặp còn lại làm bất đẳng thức sai.' % (a, x0, b, y0, a * x0 + b * y0, a * x0 + b * y0, op, c))

def i_which(r, lv):
    while True:
        px, py = r.randint(-3, 4), r.randint(-3, 4); items = []
        for _ in range(4):
            a = r.choice([1, 2, 3, -1, -2]); b = r.choice([1, 2, -1, -3]); c = r.randint(-4, 8); op = r.choice(list(OPS)); items.append((a, b, op, c))
        if len(set(items)) == 4 and sum(OPS[o](a * px + b * py, c) for a, b, o, c in items) == 1: break
    ans = [OPS[o](a * px + b * py, c) for a, b, o, c in items].index(True)
    return dict(en='The point \\(P(%d;%d)\\) belongs to the solution region of which inequality?' % (px, py), vi='Điểm \\(P(%d;%d)\\) thuộc miền nghiệm của bất phương trình nào?' % (px, py), opts=[ineq(*it) for it in items], ans=ans,
      ee='Substitute \\(x=%d\\), \\(y=%d\\) into each inequality; only the chosen one is true.' % (px, py), ev='Thay \\(x=%d\\), \\(y=%d\\) vào từng bất phương trình; chỉ bất phương trình được chọn đúng.' % (px, py))

def i_bound(r, lv):
    while True:
        a = r.choice([1, 2, 3, -1, -2]); b = r.choice([1, 2, -1, -3]); c = r.randint(-4, 8); x0 = r.randint(-3, 4)
        if (c - a * x0) % b == 0: break
    y0 = (c - a * x0) // b
    wrong = [(x0 + 1, y0), (x0, y0 + 1), (x0 - 1, y0 - 1), (x0 + 1, y0 + 1), (x0 - 1, y0 + 2)]
    wrong = [p for p in wrong if a * p[0] + b * p[1] != c]
    op = r.choice(list(OPS))
    return dict(en='The boundary line of \\(%s\\) passes through which point?' % ineq(a, b, op, c), vi='Đường thẳng biên của bất phương trình \\(%s\\) đi qua điểm nào?' % ineq(a, b, op, c),
      opts=[pt(x0, y0)] + [pt(*p) for p in wrong[:3]], ans=0, ee='The boundary line is \\(%s\\). For \\(%s\\): \\(%d\\cdot%d%+d\\cdot%d=%d\\).' % (ineq(a, b, '=', c), pt(x0, y0), a, x0, b, y0, c),
      ev='Đường biên là \\(%s\\). Với \\(%s\\): \\(%d\\cdot%d%+d\\cdot%d=%d\\).' % (ineq(a, b, '=', c), pt(x0, y0), a, x0, b, y0, c))

def i_inter(r, lv):
    while True:
        a = r.choice([2, 3, 4, 5, -2, -3]); b = r.choice([2, 3, 4, -2, -5]); c = r.choice([6, 12, 8, 10, 15, 20, -6])
        if a != b and F(c, a) != F(c, b): break
    px, py = F(c, a), F(c, b); t = lambda p, q: '(%s;0),\\ (0;%s)' % (fr(p), fr(q))
    return dict(en='Where does the line \\(%s\\) meet the axes?' % ineq(a, b, '=', c), vi='Đường thẳng \\(%s\\) cắt hai trục tọa độ tại các điểm nào?' % ineq(a, b, '=', c),
      opts=pick_opts(r, t(px, py), [t(py, px), t(-px, -py), t(px, -py), t(F(a, c), F(b, c))]), ans=0,
      ee='Put \\(y=0\\): \\(x=\\dfrac{%d}{%d}\\). Put \\(x=0\\): \\(y=\\dfrac{%d}{%d}\\).' % (c, a, c, b), ev='Cho \\(y=0\\): \\(x=\\dfrac{%d}{%d}\\). Cho \\(x=0\\): \\(y=\\dfrac{%d}{%d}\\).' % (c, a, c, b))

def i_count(r, lv):
    a = r.choice([1, 2, 3]); b = r.choice([2, 3, 4, 5]); c = r.randint(10, 14 + 4 * lv)
    n = sum(1 for x in range(0, c + 1) for y in range(0, c + 1) if a * x + b * y <= c)
    others = [n - 2, n - 1, n + 1, n + 2, n + 3]
    return dict(en='How many pairs \\((x;y)\\) of natural numbers (\\(x,y\\ge0\\)) satisfy \\(%s\\)?' % ineq(a, b, '\\le', c), vi='Có bao nhiêu cặp số tự nhiên \\((x;y)\\) (\\(x,y\\ge0\\)) thỏa mãn \\(%s\\)?' % ineq(a, b, '\\le', c),
      opts=pick_opts(r, str(n), [str(o) for o in others if o != n]), ans=0, ee='For each \\(x\\) with \\(%dx\\le%d\\), count the values of \\(y\\) with \\(%dy\\le%d-%dx\\). The total is %d.' % (a, c, b, c, a, n),
      ev='Với mỗi \\(x\\) thỏa \\(%dx\\le%d\\), đếm các giá trị \\(y\\) thỏa \\(%dy\\le%d-%dx\\). Tổng cộng có %d cặp.' % (a, c, b, c, a, n))

def i_model(r, lv):
    a = r.choice([3, 4, 5, 6, 8]); b = r.choice([2, 7, 9, 10, 12]); c = r.choice([40, 50, 60, 80, 100]); w = r.choice([('at most', 'nhiều nhất', '\\le'), ('at least', 'ít nhất', '\\ge')])
    wrong = [ineq(b, a, w[2], c), ineq(a, b, '\\ge' if w[2] == '\\le' else '\\le', c), ineq(a, b, '<' if w[2] == '\\le' else '>', c)]
    return dict(en='A notebook costs %d thousand dong and a pen costs %d thousand dong. Mai spends %s %d thousand dong on \\(x\\) notebooks and \\(y\\) pens. Which inequality describes this?' % (a, b, w[0], c),
      vi='Một quyển vở giá %d nghìn đồng, một cái bút giá %d nghìn đồng. Mai mua \\(x\\) quyển vở và \\(y\\) cái bút hết %s %d nghìn đồng. Bất phương trình nào mô tả điều đó?' % (a, b, w[1], c),
      opts=[ineq(a, b, w[2], c)] + wrong, ans=0, ee='The total cost is \\(%dx+%dy\\) and it must be %s %d: \\(%s\\).' % (a, b, w[0], c, ineq(a, b, w[2], c)), ev='Tổng tiền là \\(%dx+%dy\\) và phải %s %d: \\(%s\\).' % (a, b, w[1], c, ineq(a, b, w[2], c)))

B3 = [i_point, i_which, i_bound, i_inter, i_count, i_model, i_point, i_count]
