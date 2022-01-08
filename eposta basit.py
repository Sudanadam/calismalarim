import ssl
import smtplib

kullanici = "hamicankizilkan@gmail.com"
sifre = "Hc201012."

alici = "hamicankizilkan@hotmail.com"
mesaj = "deneme mesajı"
baslık = "Pythom gönderisi"

context = ssl.create_default_context()
port = 465
host = "smtp.gmail.com"
eposta_sunucusu = smtplib.SMTP_SSL(host=host, port=port, context=context)
eposta_sunucusu.login(kullanici, sifre)
eposta_sunucusu.sendmail(kullanici, alici, mesaj)
