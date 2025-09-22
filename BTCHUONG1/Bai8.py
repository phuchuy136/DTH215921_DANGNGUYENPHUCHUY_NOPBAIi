n = 4
for i in range(n):
    if i==0 or i == n - 1: #dòng  đầu hoặc cuối
        print("*" * n)
    else: #các dòng giữa
        print("*"  + " " * (n-2) + "*")