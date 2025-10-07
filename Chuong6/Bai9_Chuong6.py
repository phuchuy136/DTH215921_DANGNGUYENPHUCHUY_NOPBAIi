'''
Xử lý mảng
Yêu cầu:
Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:
- Dòng 1 : gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.
- Dòng 2 : gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.
- Dòng 3 : gồm các số nguyên tố.
- Dòng 4 : gồm các số không phải là số nguyên tố.
M[] ={3,6,7,8,11,17,2,90,2,5,4,5,8}
➔ 3, 7, 11,17, 5(2) ➔6 số lẻ
'''
n = int(input("Nhap so phan tu của list:"))
lst=[]

for i in range(n):
        x=int(input(f"Nhap phan tu thu {i+1}:"))
        lst.append(x)
        
def SoLe(x):
        if x%2==0:
            return False
        return True
tamle=[]
demle=0
tamchan=[]
demchan=0
for i in range(n):
    if SoLe(lst[i]):
        demle=demle+1
        tamle.append(lst[i])
    else:
        demchan=demchan+1
        tamchan.append(lst[i])
print("Danh sach so le la:")
print(tamle)
print("Co",demle,"so le trong list")

print("Danh sach so chan la:")
print(tamchan)
print("Co",demchan,"so chan trong list")


def CheckPrime(n):
    d=0
    for i in range(1,n+1):
        if n%i ==0:
            d+=1
    return d==2

demnt=0
tamnt=[]
demknt=0
tamknt=[]
for i in range(n):
    if CheckPrime(lst[i]):
        demnt+=1
        tamnt.append(lst[i])
    else:
        demknt+=1
        tamknt.append(lst[i])
print("Danh sach so nguyen to la:")
print(tamnt)
print("Có ",demnt,"số nguyên tố trong list")

print("Danh sach so khong phai so nguyen to la:")
print(tamknt)
print("Có ",demknt,"số không phải so nguyên tố trong list")

print("Danh sach vua nhap la:")
print(lst)