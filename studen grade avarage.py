n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

gradelist = list(student_marks[input()])
sum = 0
for grade in range(len(gradelist)):
    sum += gradelist[grade]

print("{0:.2f}".format(sum / 3))

