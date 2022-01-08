from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib

kullanici = "hamicankizilkan@gmail.com"
sifre = "Hc201012."
baslik = "Pythom gönderisi"
mesaj = "deneme mesajı"
context = ssl.create_default_context()
alici = "hamicankizilkan@hotmail.com"

posta = MIMEMultipart()
posta["From"] = kullanici
posta["To"] = alici
posta["Subject"] = baslik

posta.attach(MIMEText(mesaj, "plain"))
eklenti_dosya_ismi = "2 (1).jpg"

with(open(eklenti_dosya_ismi, "rb")) as eklenti_dosyasi:
    payload = MIMEBase("application", "octate-stream")
    payload.set_payload((eklenti_dosyasi).read())
    encoders.encode_base64(payload)

    payload.add_header("Content-Decomposition", "attachment", filename = eklenti_dosya_ismi)
    posta.attach(payload)

    posta_str = posta.as_string()
    port = 465
    host = "smtp.gmail.com"
    eposta_sunucusu = smtplib.SMTP_SSL(host=host, port=port, context=context)
    eposta_sunucusu.login(kullanici, sifre)
    eposta_sunucusu.sendmail(kullanici, alici, posta_str)