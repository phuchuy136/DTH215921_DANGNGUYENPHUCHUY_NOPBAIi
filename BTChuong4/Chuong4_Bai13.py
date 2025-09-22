#Kiểm tra số hoàn thiện, số thịnh vượng
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.") 
else:
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    if tong_uoc == n:
        print(f"{n} là số hoàn thiện.")
    else:
        print(f"{n} không phải là số hoàn thiện.")
    if tong_uoc > n:
        print(f"{n} là số thịnh vượng.")
    else:
        print(f"{n} không phải là số thịnh vượng.")