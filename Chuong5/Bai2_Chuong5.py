#Viết chưuong trình tối ưu chuỗi 
'''
Một chuỗi là tối ưu khiL Không chứa các khoảng trắng dưa thừa, các từ cách nhau 
bởi 1 khoảng trắng
'''
def ToiUuChuoi(s):
    s2 = s
    s2 = s2.strip()
    arr = s2.split(' ')
    s2 = ""
    for x in arr: 
        word = x
        if len(word.strip()) !=0:
            s2 = s2 + word + " "
    return s2.strip()

s = "   Hứa   Quang   Hán   "
print(s,"=>",len(s))
s = ToiUuChuoi(s)
print(s,"=>",len(s))
