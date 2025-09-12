# Tinh diem trung binh 
#Nhap diem 3 mon toan ly hoa. in ra dtb voi 2 so le thap phan 
t = float(input("Nhập điểm toán = "))
l = float(input("Nhập điểm lý = "))
h = float(input("Nhập điểm hoá = "))
dtb = float((t+l+h)/3)
print("Toán: ",t,"Lý: ",l,"Hoá: ",h)
print("Điểm trung bình 3 môn = ", dtb)
print("Điểm trung bình 3 môn (làm tròn) = ", round(dtb,2))