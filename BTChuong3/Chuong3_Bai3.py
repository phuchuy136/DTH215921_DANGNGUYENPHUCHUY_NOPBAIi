#viet chuong trinh giai phuong trinh bac 2 
import math

print("Chương trình giải phương trình bậc 2: ")
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

if a == 0: 
    if b == 0: 
        if c == 0: 
            print("PT VSN")
        else: 
            print("PT VN")
    else: 
        x = -c/b
        print("PT có 1 nghiệm x = ", x)
else: 
    delta = a*a - 4*a*c
    if delta > 0: 
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("PT có 2 nghiệm phân biệt x1 = ",x1,"; x2 = ", x2)
    elif delta == 0:
        x = -b/(2*a)
        print("PT có nghiệm kép x1 = x2 = ", x)
    else: 
        print("PT VN")