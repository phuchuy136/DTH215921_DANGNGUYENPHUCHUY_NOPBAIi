#viết hàm tính BMI
'''
Gọi BMI là chỉ số cân đối cơ thể, 
Yêu cầu nhập vào chiều cao, cân nặng.
Hãy cho biết người ngày như thế nào. 
'''
def MBI(height, weight):
    return weight/(height**2)
def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi < 24.9:
        return "Bình thường"
    elif bmi < 29.9:
        return "Hơi béo"
    elif bmi < 34.9:
        return "Béo phì cấp độ 1"
    elif bmi < 39.9:
        return "Béo phì cấp độ 2"   
    else:
        return "Béo phì cấp độ 3"
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Nguy cơ thấp"
    elif bmi <= 24.9:
        return "Nguy cơ trung bình"
    elif bmi <= 29.9:
        return "Nguy cơ cao"
    elif bmi <= 34.9:
        return "Nguy cơ rất cao"
    elif bmi <= 39.9:
        return "Nguy cơ cực kỳ cao"   
    else:
        return "Nguy hiểm"
    
print("==Chương trình tính chỉ số BMI==")
print("Nhap chiều cao (m): ")
height = float(input())
print("Nhập cân nặng (kg): ")
weight = float(input())
bmi = MBI(height, weight)
print(f"Chỉ số BMI = {bmi}")
print(f"Phân loại: {PhanLoai(bmi)}")
print(f"Nguy cơ bệnh: {NguyCoBenh(bmi)}")