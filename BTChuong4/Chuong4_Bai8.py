#Viết chương trình tính logax
'''
Viết hàm tính logarit với a, x là các số nhập từ bàn phím.
x>0, a>0 và a!=1
logax = ln(x)/ln(a)
'''
import math
def log(a, x):
    return math.log(x)/math.log(a)
print("==Chương trình tính logarit==")
a = float(input("Nhập cơ số a (a>0 và a!=1): "))
#kiểm tra a
while a <= 0 or a == 1:
    a = float(input("Nhập lại cơ số a (a>0 và a!=1): "))
    
x = float(input("Nhập x (x>0): "))
#kiểm tra x
while x <= 0:
    x = float(input("Nhập lại x (x>0): "))

print(f"log{a}({x}) = {log(a, x)}")
