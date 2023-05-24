
sys_kullaniciadi = "huseyin"
sys_parola = "123456"

giris_hakki = 3


while True:
    kullaniciadi = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if (sys_kullaniciadi == kullaniciadi and sys_parola == parola):
        print("Giriş Yapılıyor")
        break
    elif (sys_kullaniciadi != kullaniciadi or sys_parola != parola):
        giris_hakki -= 1
        print("Şifre Hatalı")
    if (giris_hakki == 0):
        print("Giriş Hakkınız Bitti")
        break

