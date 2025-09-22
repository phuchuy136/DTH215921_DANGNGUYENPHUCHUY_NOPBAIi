#Viết chương trình tính căn bậc hai lồng nhau
'''
Nhập n, tính S(n) = √(2√(2√(2...√2))) (n dấu căn)
'''
import math
def canbachai(n):
    if n == 1:
        return math.sqrt(2)
    else:
        return math.sqrt(2 * canbachai(n - 1))
print("==Chương trình tính căn bậc hai lồng nhau==")
n = int(input("Nhập n (n>0): "))
#kiểm tra n
while n <= 0:
    n = int(input("Nhập lại n (n>0): "))
print(f"S({n}) = {canbachai(n)}")
    