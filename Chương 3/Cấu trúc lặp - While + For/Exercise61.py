avg_list = []
m = int(input())

if m!=0:
    avg_list.append(m)
    while True:
        n = int(input())
        if n==0:
            avg = sum(avg_list)/len(avg_list)
            print('Average = %s'%(avg))
            break
        avg_list.append(n)
else:
    print('Error')