q = int(input('Enter decimal value:'))
x = q
k = []
while q > 0:
    r = int(float(q % 2))
    k.append(r)
    q = (q-r)/2
k.append(0)
result = ""
for j in k[::-1]:
    result = result + str(j)
print('The binary for', x, 'is', result)
