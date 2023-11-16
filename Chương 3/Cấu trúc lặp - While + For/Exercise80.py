from random import seed
from random import randint
sum=0
for i in range(1, 10):
    list = []
    seed(i)
    while True:
        value = randint(0, 1)
        list.append(value)
        if len(list) >=3:
            if list[-1] == list[-2] == list[-3]:
                break
    for i in range(len(list)):
        if list[i] == 0:
            print("H", end=" ")
        else:
            print("T", end=" ")
    print("(", len(list), "flips)")
    sum += len(list)
average = sum/10
print("On average,", average, "flips were needed")