c4_fre=261.63
d4_fre=293.66
e4_fre=329.63
f4_fre=349.23
g4_fre=392.00
a4_fre=440.00
b4_fre=493.88
lim=1

fre=float(input("Enter the frequency: "))

if fre>=c4_fre-lim and fre<=c4_fre+lim:
    note="C4"
elif fre>=d4_fre-lim and fre<=d4_fre+lim:
    note="D4"
elif fre>=e4_fre-lim and fre<=e4_fre+lim:
    note="E4"
elif fre>=f4_fre-lim and fre<=f4_fre+lim:
    note="F4"
elif fre>=g4_fre-lim and fre<=g4_fre+lim:
    note="G4"
elif fre>=a4_fre-lim and fre<=a4_fre+lim:
    note="A4"
elif fre>=b4_fre-lim and fre<=b4_fre+lim:
    note="B4"
else:
    note=""

if note=="":
    print("Undefined frequency!")
else:
    print("The frequency is",note)
