python_students = {}
for i in range(int(input("kaç kişi var: "))) :
    name = input("bir isim giriniz: ")
    score = float(input("bir not giriniz: "))
    python_students[name] = score

sl = sorted(list(set(sorted(python_students.values()))))[1]
for key, value in sorted(python_students.items()):
    if value == sl:
        print(key)