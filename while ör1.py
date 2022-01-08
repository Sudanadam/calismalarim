import random
list_even = []
list_odd = []
rand_list = []
rand_list2 = []
def creat_random_work() :
    rand_list2.append(random.randint(-1, 20))
    n = max(rand_list2)
    print(n)
    for i in range(n):
        rand_list.append(random.randint(-1, 100))
        rand_list.sort()
    #print(rand_list)
def number_check() :
    for number in rand_list:
        if number % 2 == 0 and number != 0:
            list_even.append(number)
        elif number % 2 == 1:
            list_odd.append(number)
        elif number == 0:
            print("This number is zero")
creat_random_work()
number_check()
print(list_even)
print(list_odd)