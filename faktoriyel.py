print("Faktöriyel Hesaplama Programı")

print("Çıkmak için 0' basınız")

sayi = int(input("Sayı Giriniz: "))

while True:
    if(sayi == 0):
        print("Programdan çıkılıyor...")
        break
    else:
        faktoriyel = 1
        for i in range(1, sayi+1):
            faktoriyel *= i
        print("Faktöriyel: ", faktoriyel)
        sayi = int(input("Sayı Giriniz: "))