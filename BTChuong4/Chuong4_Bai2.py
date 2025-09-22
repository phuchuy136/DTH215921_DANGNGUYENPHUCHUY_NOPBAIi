#Viết hàm chơi game đoán số 
'''
máy ra 1 số trong đoạn [1...100], người chơi đoán số, chỉ được
sai 7 lần. Mỗi lần đoán sẽ thông báo số người chơi đoán nhỏ hơn hay lớn hơn
số của máy và hiển thị số lần đoán. 
End game khi sai quá 7 lần hoặc đoán trúng trước 7 lần. 
Sau khi endgame hỏi người chơi có tiếp tục hay không? 
'''
from random import randrange
while True: 
    somay = randrange(1,101)
    solandoan = 0
    win = False
    while solandoan<7:
        solandoan+=1
        songuoi = int(input("Máy đoán [1...100], mời bạn đoán-> "))
        print(f"Lần đoán thứ {solandoan}:")
        if somay == songuoi:
            print(f"\t=> Chúc mừng bạn đoán đúng, số máy đoán là: {somay}")
        elif songuoi > somay:
            print("\=> Đoán sai, số bạn đoán > số máy!")
        elif songuoi < somay: 
            print("\t=> Đoán sai, số bạn đoán < số máy!")
    if win == False:
        print(f"GAME OVER!, số máy đoán là {somay}")
    hoi = input("Bạn có muốn tiếp tục chơi không?")
    if hoi == "k":
        break
print("Cảm ơn bạn đã tham gia trò chơi!")