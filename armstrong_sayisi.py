print("Armstrong Sayısı Bulucu")

sayi = int(input("Lütfen bir sayı giriniz:"))
sayi_uzunluk = len(str(sayi))
toplam = 0

if sayi_uzunluk == 3:
    for i in str(sayi):
        toplam += int(i)**int(sayi_uzunluk)
    if (toplam == sayi):
        print(sayi,", bir Armstrong sayısıdır.")
    else:
        print(sayi,", bir Armstrong sayısı değildir.")
elif sayi_uzunluk == 4:
    for i in str(sayi):
        toplam += int(i)**int(sayi_uzunluk)
    if (toplam == sayi):
        print(sayi,",  bir Armstrong sayısıdır.")
    else:
        print(sayi,", bir Armstrong sayısı değildir.")
else:
    print("3 ya da 4 rakamlı sayı girin")




        
    
