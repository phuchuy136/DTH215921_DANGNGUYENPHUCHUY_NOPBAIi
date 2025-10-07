#Trích lọc số âm trong chuỗi 
'''
Câu 6: Trích lọc số âm trong chuỗi
Yêu cầu:
Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào
là một chuỗi bất kỳ, Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên
âm đó là -5 và -12
'''
import re
def NegativeNumberInStrings(s):
    #Tìm tất cả só nguyên âm, không tính "--" hoặc các dấu trừ không hợp lê
    numbers = re.findall(r'-(\d+)', s)
    for num in numbers:
        print(f"-{num}")

s = input("Nhập chuỗi: ")
NegativeNumberInStrings(s)