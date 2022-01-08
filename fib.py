n = int(input("sayı gir: ")) #0 1 1 2 3
def fib(n):
    ilk  = 0
    ikinci = 1
    list1 = [0,1]
    #print(ilk)
    #print(ikinci)
    top1 = 0
    for i in range(2,n):
        sonuc = ilk + ikinci
        ilk = ikinci
        ikinci = sonuc
        list1.append(sonuc)
        top1 = sum(list1)
        #print(sonuc)
    print(top1)
fib(n)

