K1 = int(input("Masukkan jumlah kill player pertama: "))
D1 = int(input("Masukkan jumlah death player pertama: "))
A1 = int(input("Masukkan jumlah assists player pertama: "))

KDA1 = K1+(A1*0.75)-(D1*0.5)
if(KDA1 > 10):
    rank1 = 'GOLD'
elif(KDA1 <=10 and KDA1 >=6):
    rank1 = 'SILVER'
else:
    rank1 = 'BRONZE'

K2 = int(input("Masukkan jumlah kill player kedua: "))
D2 = int(input("Masukkan jumlah death player kedua: "))
A2 = int(input("Masukkan jumlah assists player kedua: "))

KDA2 = K2+(A2*0.75)-(D2*0.5)
if(KDA2 > 10):
    rank2 = 'GOLD'
elif(KDA2 <=10 and KDA2 >=6):
    rank2 = 'SILVER'
else:
    rank2 = 'BRONZE'

K3 = int(input("Masukkan jumlah kill player ketiga: "))
D3 = int(input("Masukkan jumlah death player ketiga: "))
A3 = int(input("Masukkan jumlah assists player ketiga: "))

KDA3 = K3+(A3*0.75)-(D3*0.5)
if(KDA3 > 10):
    rank3 = 'GOLD'
elif(KDA3 <=10 and KDA3 >=6):
    rank3 = 'SILVER'
else:
    rank3 = 'BRONZE'

print('Rank Player Pertama: ', rank1)
print("KDA Player Pertama: ", KDA1)
print('Rank Player Kedua: ', rank2)
print("KDA Player Kedua: ", KDA2)
print('Rank Player Ketiga: ', rank3)
print("KDA Player Ketiga: ", KDA3)

