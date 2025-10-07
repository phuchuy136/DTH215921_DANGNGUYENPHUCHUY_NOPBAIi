'''
Câu 7: Tối ưu chuỗi danh từ
Yêu cầu:
Viết chương trình tối ưu Chuỗi danh từ
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
Ví dụ:
Input “ TRần duY thAnH ”
Output “Trần Duy Thanh”

'''
s = input("Nhập chuỗi: ")
s = s.strip()  # Xóa khoảng trắng đầu và cuối
words = s.split()  # Tách chuỗi thành các từ
optimized_words = [word.capitalize() for word in words]  # Viết hoa chữ cái đầu của mỗi từ
optimized_string = ' '.join(optimized_words)  # Nối các từ lại với nhau bằng một khoảng trắng
print("Chuỗi tối ưu:", optimized_string)