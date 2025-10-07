'''
Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp
dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.
'''
n = int(input("Nhập số lượng phần tử: "))
lst=[]
for i in range(n):
        x = float(input("Nhập phần tử: "))
        lst.append(x)

print("List đã nhập: ")
print(lst)

lst.sort(reverse=True)

print("List đã sắp xếp: ")
print(lst)

