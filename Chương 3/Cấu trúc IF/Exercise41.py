ky_tu = str(input('Nhập ký tự:'))
so = int(input('Nhập số:'))
name = str(ky_tu) + str(so)
print(name)
a4 = 440.00
b4 = 493.88
c4 = 261.63
d4 = 293.66
e4 = 393.63
f4 = 349.23
g4 = 392.00
if name == 'C4':
    print(c4, 'Hz')
elif name == 'D4':
    print(d4, 'Hz')
elif name == 'E4':
    print(e4, 'Hz')
elif name == 'F4':
    print(f4, 'Hz')
elif name == 'G4':
    print(g4, 'Hz')
elif name == 'A4':
    print(a4, 'Hz')
elif name == 'B4':
    print(b4, 'Hz')
elif ky_tu == 'C' and 0 <= so <= 8:
    x = so
    tan_so = c4/(2**(4-x))
    print(tan_so, 'Hz')

