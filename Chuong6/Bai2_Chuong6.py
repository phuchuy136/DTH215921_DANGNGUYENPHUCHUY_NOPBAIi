from random import randrange

lst = []
print("Nhập số phần tử: ")
n = int(input())
for i in range(n):
    lst.append(randrange(0,100))
print("List sau khi tạo ngẫu nhiên là: ")
print(lst)
x = int(input("Chèn thêm số mới: "))
lst.append(x)
print("List mới sau khi chèn: ")
print(lst)
k=int(input("Nhập số muốn xoá: "))
while lst.count(k)>0:
    lst.remove(k)
print("List sau khi ",k," được xoá: ")
print(lst)

def KTDoiXung(lst):
    for i in range (len(lst)):
        if lst[i]!=lst[len(lst)-i-1]:
            return False
        return True

kt = KTDoiXung(lst)
if kt == True:
    print("=>> List đối xứng.")
else:
    print("=>> List không đối xứng.")