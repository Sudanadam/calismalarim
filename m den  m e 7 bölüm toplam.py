while True:
    n = int(input("1. sayı: "))
    m = int(input("2. sayı: "))
    if n >= m :
        print("n küçük olmalı.tekrar gir")
    else:
        break

toplam = 0

for i in range(n,m+1):
    if i %7 == 0 :
        toplam = toplam + i
    else:
        None
print("toplam bu",toplam)
