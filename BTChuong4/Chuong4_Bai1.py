#viết hàm tính diện tích tam giác 
'''
Nhập 3 cạnh, kiểm tra tính hợp lệ,
sau đó tính diện tích theo công thức herong
'''
from math import sqrt

print("==Chương trình tính diện tích tam giác==")
a = float(input("Nhập cạnh a>0: "))
b = float(input("Nhập cạnh b>0: "))
c = float(input("Nhập cạnh c>0: "))

#kiểm tra
if (a<=0 or b<=0 or c<= 0) or (a+b)<=c or (a+c)<=b or (b+c)<=a:
    print("=> Tam giác không hợp lệ")
else: 
    cv = a + b + c
    p = cv/2
    dt = sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"=> Diện tích tam giác = {dt}")