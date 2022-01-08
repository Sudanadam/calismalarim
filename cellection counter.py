from collections import Counter
in1 = int(input("kaç tane ayakkabı var: "))                      #3
in2 = list(input("ayakkabı numaraları nedir: ").split(" "))      #2 3 4
print(in2)                                                       #['2', '3', '4']

a =  dict(Counter(in2))
print(a)                                                           #{'2': 1, '3': 1, '4': 1}
# aa = a.most_common()
# print(aa)                                                        #[('2', 1), ('3', 1), ('4', 1)]

in3 = int(input("kac tane alacaksın: "))                         # 2

borcu = 0
for i in range(in3):
    in4 = list(input("size ve fiyat gir: ").split(" "))             # 2 50  ['2', '50']
    if (in4[0] in in2) and (a[in4[0]] >= 1):                         #in4[0] = 2,    ['2', '3', '4']
        borcu = borcu + int(in4[1])
        a[in4[0]] = a[in4[0]] - 1
    else:
        None
print("borcunuz : ",borcu)





# 2 3 4 5 6 8 7 6 5 18
# 3
# 2 3 4
# 1
# 2 50