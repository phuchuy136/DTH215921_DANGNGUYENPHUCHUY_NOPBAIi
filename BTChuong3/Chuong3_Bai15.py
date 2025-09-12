#giải thích các dòng lệnh range
cases = [
    ("(a)", range(5)),
    ("(b)", range(5, 10)),
    ("(c)", range(5, 20, 3)),
    ("(d)", range(20, 5, -1)),
    ("(e)", range(20, 5, -3)),
    ("(f)", range(10, 5)),
    ("(g)", range(0)),
    ("(h)", range(10, 101, 10)),
    ("(i)", range(10, -1, -1)),
    ("(j)", range(-3, 4)),
    ("(k)", range(0, 10, 1))
]

for key, r in cases:
    print(f"{key} {r} -> {list(r)}")
