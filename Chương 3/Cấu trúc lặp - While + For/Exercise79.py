import random
i = 0
a_max = 0
random_num = 0
update_times = 0
while i <= 100:
    i += 1
    random_num = random.randint(1, 100)
    if random_num > a_max:
        a_max = random_num
        update_times += 1
        print(a_max, '<== Update')
    else:
        print(random_num)
print('The maximum value found was', a_max)
print('The maximum value was updated', update_times, 'times')