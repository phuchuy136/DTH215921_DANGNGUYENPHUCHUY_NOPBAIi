# Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai
#quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong 
n = int(input("Nhập số lượng phần tử: "))
lst=[]
for i in range(n):
    while True: 
        x = int(input("Nhập phần tử: "))
        if(i==0 or x > lst[i-1]):
            lst.append(x)
            break
        else: 
            print("Nhập lại!")

print("List đã nhập: ")
print(lst)