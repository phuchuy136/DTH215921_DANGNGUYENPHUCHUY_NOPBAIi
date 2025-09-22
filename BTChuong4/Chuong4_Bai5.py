#Viết hàm đệ qui Fibonacci
'''
Dãy fibonacci là dãy số bắt đầu bằng 0, 1, 
sau đó số tiếp theo là tổng của 2 số liền trước nó.
Nếu N = 1, N = 2 thì F(N) = 1
Nếu N > 2 thì F(N) = F(N-1) + F(N-2)
Nếu N = 1 hoặc N = 2:
Giá trị Fibonacci tại vị trí này là 1.
Ví dụ: F(1) = 1, F(2) = 1

Nếu N > 2:
Giá trị Fibonacci tại vị trí N bằng tổng của hai số Fibonacci liền trước nó:
F(N) = F(N-1) + F(N-2)

Ví dụ:

F(3) = F(2) + F(1) = 1 + 1 = 2
F(4) = F(3) + F(2) = 2 + 1 = 3
F(5) = F(4) + F(3) = 3 + 2 = 5
'''

def fibonacci(n):
    if n<= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def listfibo(n):
    for i in range(1,n+1):
        print(fibonacci(i), end = '\t')

print(fibonacci(9))
listfibo(9)