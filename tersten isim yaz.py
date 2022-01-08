isim = input("isim giriniz: ")
uzunluk = len(isim)
print("ismin uzunluğu : ", uzunluk)

tersten_isim = ""
for i in range(uzunluk-1,-1,-1):
    tersten_isim = tersten_isim + isim[i]
print(tersten_isim)