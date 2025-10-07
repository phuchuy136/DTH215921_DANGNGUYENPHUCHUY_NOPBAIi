#Câu 1: Xử lý list
'''
Viết chương trình cho phép:
- Khởi tạo list
- Thêm phần tử vào list
- Nhập k, kiểm tra k xuất hiện bao nhiêu lần trong list
- Tính tổng các số nguyên tố trong list
- Sắp xếp
- Xóa list
'''

from random import randrange

print("Chương trình xử lý list: ")
n = int(input("Nhập số phần tử"))
lst=[0]*n
for i in range(n):
    lst[i]=randrange(-100,100)
print("List ngẫu nhiên là: ")
print(lst)
print("Mời bạn thêm số mới: ")
value = int(input())
lst.append(value)
print(lst)
print("Bạn muốn đếm số nào: ")
k=int(input())
dem=lst.count(k)
print(k," xuất hiện ",dem," lần trong list.")
def CheckPrime(n):
    d=0
    for i in range(1,n+1):
        if n%i == 0: 
            d+=1
    return d==2
demnt = 0
tongnt = 0
for x in lst: 
    if CheckPrime(x):
        demnt+=1
        tongnt+=x
print("Có ",demnt," số nt trong list")
print("Tổng các số nt = ", tongnt)
lst.sort()
print("List sau khi sort: ")
print(lst)

del lst
print("List sau khi xoá: ")
print("List đã được xóa thành công!")