#Cau1: Tinh chu vi dien tich hinh tron 
#Yc: Nhap ban kinh r, tinh va xuat chu vi, dien tich 
#cv = 2*pi*r va dt = pi*r*r
import math

try: 
    r = float(input("Mời bạn nhập bán kính hình tròn: "))
    cv = 2*math.pi*r
    dt = math.pi*r**2
    print("Chu vi = ", cv)
    print("Diện tích = ", dt)
except: 
    print("Chương trình có lỗi!")