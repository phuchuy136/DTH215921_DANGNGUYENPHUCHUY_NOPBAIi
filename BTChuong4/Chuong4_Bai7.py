#Tính và xuất độ dài đoạn AB
'''
Nhập toạ độ 2 điểm A(xa, ya) và B(xb, yb)
Tính độ dài đoạn AB theo công thức:
AB = sqrt((xb - xa)^2 + (yb - ya)^2)
'''
import math
def do_dai_AB(xa, ya, xb, yb):
    return math.sqrt(abs((xb - xa)**2 + (yb - ya)**2))
print("=== Tính độ dài đoạn AB ===")
print("Nhập toạ độ điểm A:")
xa = float(input("xa = "))
ya = float(input("ya = "))  
print("Nhập toạ độ điểm B:")
xb = float(input("xb = "))      
yb = float(input("yb = "))
print("Độ dài đoạn AB là:", do_dai_AB(xa, ya, xb, yb))