#Kiểm tra chuỗi đối xứng 
def CheckDoiXung(s):
    flag = True
    for i in range (len(s)):
        if s[i] != s[len(s)-i-1]:
            flag = False
            break
    return flag
def main():
    print("Nhập một chuỗi: ")
    s = input()
    if(CheckDoiXung(s)):
        print("Chuỗi vừa nhập đối xứng!")
    else: 
        print("Chuỗi vừa nhập không đối xứng!")
while True: 
    main()
    print("Tiếp khum bà? (say c/k): ")
    s = input()
    if s == "k":
        break
print("Thén kìu!")