#Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo
#đúng phép toán đã nhập
a = float(input("Nhập số a: "))
b = float(input("Nhập số B: "))
pt = input("Nhập phép tính (+, -, *, /): ")

if pt not in ["+","-","*","/"]:
    print("Phép tính sai!")
elif pt == "+":
    kq = a + b
elif pt == "-":
    kq = a - b
elif pt == "*":
    kq = a * b
elif pt == "/":
    kq = a / b

print(f"Kết quả của phép tính {a} {pt} {b} = {kq}")