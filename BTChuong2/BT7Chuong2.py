#cau 7: 
print("Câu hỏi: Trình bày một số cách nhập dữ liệu từ bàn phím")
print("Cách 1: Hàm input()) - Nhập chuỗi từ bàn phím")
ten = input("Nhập tên của bạn: ")
print("Tên của bạn là ", ten)
print("----")
print("Cách 2: Ép kiểu bằng int(), float(),...")
tuoi = int(input("Nhập tuổi: ")) #Nhập số nguyên
cao = float(input("Nhập chiều cao: ")) #nhập số thực
print("Chiều cao là ", cao," và tuổi là ", tuoi)
print("----")
print("Cách 3: Nhập nhiều giá trị trên 1 dòng split())")
a, b = input("Nhập hai số cách nhau bởi dấu cách: ").split()
print("Có thể ép kiểu luôn: ")
c, d = map(int, input("Nhập 2 số: ").split())
print("Các số: ",a, b, c, d)


