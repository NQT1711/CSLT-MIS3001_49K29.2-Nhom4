a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if (a +b )> c and (a + c)> b and (b + c) > a and (a > 0) and (b > 0) and (c > 0):
    if (a*a == b * b + c * c) or (b * b == a * a + c * c) or (c * c == a * a + b * b):
        print('Tam giac vuong')
    elif (a == b) or (b == c) or (c == a):
        print('Tam giac deu')
    elif a==b or a==c or b==c:
        print('tam giac can')
    else:
        print('Tam giac loai khac')
else:
    print('Khong hop le')