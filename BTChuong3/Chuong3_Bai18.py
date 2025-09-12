#vẽ hình 
print("Chữ nhật: ")
n = 4
for i in range(n):
    if i == 0: 
        print("*"*4)
    elif i ==1 or i ==2: 
        print("*"+" "*2+"*")
    elif i == 3: 
        print("*"*4)

print("Tam giác: ")
n = 5
for i in range(n):
    if i == 0: 
        print(" "+" "+" "+"*")
    elif i ==1: 
        print(" "*2+"*"*2)
    elif i == 3: 
        print(" "+"*"*3)
    elif i == 4: 
        print("*"*4)

print("Hai tam giác:")
n = 8
for i in range(n):
    if i == 0: 
        print("*")
    elif i ==1: 
        print("*"*2+" "*2)
    elif i == 2: 
        print("*"+" "+"*")
    elif i == 3: 
        print("*"*7)
    elif i == 4: 
        print(" "*4+"*"+" "+"*")
    elif i == 5: 
        print(" "*5+"*"*2)
    elif i == 6:
        print(" "*6+"*")

