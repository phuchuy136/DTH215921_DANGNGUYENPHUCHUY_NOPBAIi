print("--Chương trình kiểm tra năm nhuần--")
nam = int(input("Nhập vào một năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0: 
    print(f"Năm {nam} là năm nhuần!")
else: 
    print(f"Năm {nam} không phải năm nhuần!")
