python_students = {}
for i in range(int(input("kaç kişi var: "))):
    name = input("bir isim giriniz: ")
    score = int(input("bir not giriniz: "))
    python_students[name] = score
    i = i + 1
print(python_students)
list_of_value = list(python_students.values())
list_of_keys = list(python_students.keys())
print(max(list_of_value))
for val in python_students.values():
    if value == max(list_of_value):
        print(python_students[val])
    else:
        None
