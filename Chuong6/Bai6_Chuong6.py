#Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU
from random import randrange
from random import sample
n = int(input("Nhập số phần tử: "))

lst = sample(range(1,100), n)

print("List sau khi tạo ngẫu nhiên là: ")
print(lst)
