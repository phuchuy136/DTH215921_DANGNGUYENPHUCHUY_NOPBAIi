'''
Câu 8: Tách lấy tên bài hát
Yêu cầu:
Cho một chuỗi là đường dẫn của 1 file nhạc, ví dụ: d:\\music\muabui.mp3
Hãy viết 2 hàm để:
- Lấy ra muabui.mp3
- Lấy ra muabui
Lưu ý đường dẫn bài hát là bất kỳ. Nên khi truyền vào bài hát nào thì lấy chính xác theo
bài hát đó.
'''
import os
def lay_ten_file(duong_dan):
    return os.path.basename(duong_dan)
def lay_ten_bai_hat(duong_dan):
    ten_file = os.path.basename(duong_dan)
    ten_bai_hat, _ = os.path.splitext(ten_file)
    return ten_bai_hat
duong_dan = input("Nhập đường dẫn file nhạc: ")
ten_file = lay_ten_file(duong_dan)
ten_bai_hat = lay_ten_bai_hat(duong_dan)
print("Tên file:", ten_file)
print("Tên bài hát:", ten_bai_hat)

