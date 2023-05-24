print("ATM PROGRAMINA HOSGELDINIZ: 1> Bakiye Sorgulama 2> Para Çekme 3> Para Yatırma 4> Çıkış Yap")

bakiye = 1000

while True:
    islem = int(input("İslemi Seciniz: "))
    if(islem == 4):
        print("Tekrar görüşmek üzere...")
        break
    elif(islem == 1):
        print("Bakiyeniz: ", bakiye)
    elif(islem == 2):
        miktar = int(input("Miktar: "))
        if(miktar > bakiye):
            print("Bakiyeniz yetersiz")
            continue
        bakiye -= miktar
    elif(islem == 3):
        miktar = int(input("Miktar: "))
        bakiye += miktar
    else:
        print("Hatali islem")
    
