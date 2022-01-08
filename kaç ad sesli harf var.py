isim = input("isim giriniz :")
sesliler = "aeıiouöü"
sonuç = 0
for i in isim:
    if i in sesliler:
        sonuç = sonuç +1
    else:
        None
print("sonuç",sonuç)
