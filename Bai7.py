import sys
#kiểm tra tham số
if len(sys.argv) > 1:
    #Ghép các tham số lại với nhau (Bỏ tên file)
    input_string = " ".join(sys.argv[1:])
    print("Chuỗi bạn nhập là: ", input_string)
else: 
    print("Vui lòng nhập chuỗi khi chạy chương trình.")