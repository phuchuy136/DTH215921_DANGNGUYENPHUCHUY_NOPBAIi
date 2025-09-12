#tinh gio phut giay 
#Nhap so giay t bat ky, tinh va xuat ra dang: Gio:Phut:Giay
#VD: Nhap 3750 giay thi xuat ra 1:2:30 AM 
#HD: hour = (t/3600)%24; minute = (t%3600)/60; second = (t%3600)%60
t=int(input("Nhập số giây: "))
hour = (t//3600)%24
minute = (t%3600)//60
second = (t%3600)%60
print(hour,":",minute,":",second)