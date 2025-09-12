n, m = 0, 100 
while n!=m:
    n = int(input("Nhập số (âm để thoát hoặc 100 để dừng): "))
    if n<0: 
        break #thoát vòng lặp khi gặp số âm
    print("n = ", n)