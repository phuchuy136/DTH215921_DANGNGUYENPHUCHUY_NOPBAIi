#nhập một tháng, xuất ra tháng đó thuộc quý mấy trong năm
thang = int(input("Nhập một tháng: "))
if 1<= thang <= 12: 
    if thang in [1,2,3]:
        quy = 1
    elif thang in [4,5,6]:
        quy = 2
    elif thang in [7,8,9]:
        quy = 3
    else: 
        quy = 4

    print(f"Tháng {thang} thuộc quý {quy} trong năm.")
else: 
    print("Tháng không hợp lệ!")