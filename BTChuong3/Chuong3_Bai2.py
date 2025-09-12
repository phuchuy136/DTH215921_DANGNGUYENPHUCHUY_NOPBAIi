'''
bai2: Nhap mot thang, xuat ra thang do co bao nhieu ngay
'''
print("--Chương trình đếm ngày trong tháng--")
month = int(input("Nhập một tháng: "))
if month in (1,3,5,7,8,10,12):
    print(f"Tháng {month} có 31 ngày.")
elif month in (4,6,9,11):
    print(f"Tháng {month} có 30 ngày.")
elif month == 2: 
    year = int(input("Nhập năm: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: 
        print(f"Năm {year} là năm nhuần, tháng {month} có 29 ngày.")
    else: 
        print(f"Năm {year} không phải năm nhuận, tháng {month} có 28 ngày.")
else: 
    print(f"Tháng {month} không hợp lệ!")