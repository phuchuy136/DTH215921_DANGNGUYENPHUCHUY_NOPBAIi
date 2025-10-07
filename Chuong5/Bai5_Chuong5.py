#Xử lý chuỗi với các hàm cơ bản 
'''
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ IN HOA
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là Nguyên Âm
- Bao nhiêu chữ là Phụ âm
'''
s  = input("Nhập một chuỗi: ")
dem_hoa = dem_thuong = dem_so = dem_ktdb = dem_khoangtrang = dem_nguyenam = dem_phuam = 0
nguyen_am = "aeiouAEIOU"

for c in s:
    if c.isupper():
        dem_hoa += 1
    elif c.islower():
        dem_thuong += 1
    elif c.isdigit():
        dem_so += 1
    elif c.isspace():
        dem_khoangtrang += 1
    else:
        dem_ktdb += 1
    
    if c in nguyen_am:
        dem_nguyenam += 1
    elif c.isalpha():
        dem_phuam += 1

print(f"Số chữ IN HOA: {dem_hoa}")
print(f"Số chữ in thường: {dem_thuong}")            
print(f"Số chữ là chữ số: {dem_so}")
print(f"Số chữ là ký tự đặc biệt: {dem_ktdb}")  
print(f"Số chữ là khoảng trắng: {dem_khoangtrang}")
print(f"Số chữ là Nguyên Âm: {dem_nguyenam}")
print(f"Số chữ là Phụ âm: {dem_phuam}")

