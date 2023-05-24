print("Mükemmel Sayı Bulucu")

sayi = int(input("Lütfen Sayıyı Giriniz:"))

bolenler = []

for i in range(1, sayi):
    if sayi % i == 0:
        bolenler.append(i)

bolenler_toplami = sum(bolenler)

if(bolenler_toplami == sayi):
    print("Vay canına {} sayısı mükemmel bir sayı".format(sayi))
else:
    print("Ne yazik ki {} sayısı mükkemel bir sayı değil".format(sayi))
