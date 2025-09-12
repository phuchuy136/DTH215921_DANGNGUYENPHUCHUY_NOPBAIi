i = int(input("Nhập i: "))
j = int(input("Nhập j: "))
k = int(input("Nhập k: "))
'''
(a) i = 3, j = 5, and k = 7
(b) i = 3, j = 7, and k = 5
(c) i = 5, j = 3, and k = 7
(d) i = 5, j = 7, and k =3
(e) i = 7, j = 3, and k = 5
(f) i =7, j = 5, and k = 3
'''

if i<j: 
    if j<k:
        i=j
    else: 
        j=k
else:
    if j>k:
        j=i
    else:
        i=k 
print("i = ", i," j = ", j," k = ",k)
