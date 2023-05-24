
toplam = []

while True:
    a = input("Bir sayı giriniz veya q'ya basınız:")
    if(str(a) == "q"):
        break
    else:
        toplam.append(int(a))
        
print("Total:",sum(toplam))