#hàm oscillate
def oscillate(a, b):
    for i in range(a, b):
        print(i, end=' ')
        print(b - (i - a), end=' ')
        
# Đáp án đúng:
def oscillate(a, b):
    for i in range(a, b):
        yield i
        yield b - (i - a)

for n in oscillate(-3, 5):
    print(n, end=' ')
print()