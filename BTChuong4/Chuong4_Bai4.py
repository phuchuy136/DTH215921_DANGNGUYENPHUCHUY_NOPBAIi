#Viết hàm tính ROI
'''
ROI = (Doanh thu - Chi phí)/chi phí
Viết chương trình cho phép nguoiwf dùng nhập Doanh Thu, Chi phí,
xuất ra tỉ lệ ROI (Giả sử mức ROI tối thiểu là 0.75 mới đầu tư)
'''
def ROI(dt, cp):
    return (dt - cp)/cp
def DauTu(roi):
    if roi >= 0.75:
        return "=> Nên đầu tư"
    else: 
        return "=> Không nên đầu tư"

print("==Chương trình tính ROI==")
dt = int(input("Nhập doanh thu: "))
cp = int(input("Nhập chi phí: "))
roi = ROI(dt, cp)
print(f"Doanh thu: {dt}, Chi phí: {cp}, ROI = {roi}")
print("=>>", DauTu(roi))