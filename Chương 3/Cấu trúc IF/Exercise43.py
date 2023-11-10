n = int(input("nhap so tien: "))

if  n == 1:
    a = ("co mat ong George Washington.")
elif n == 2:
    a = ("co mat ong Thomas Jefferson.")
elif n == 5:
    a = ("co mat ong Abraham Lincoln.")
elif n == 10:
    a = ("co mat ong Alexander Hamilton.")
elif n == 20:
    a = ("co mat ong Andrew Jackson.")
elif n == 50:
    a = ("co mat ong Ulysses S. Grant.")
elif n == 100:
    a = ("co mat ong Benjamin Franklin.")
else:
    a = ("khong hop le")

if a != "khong hop le":
    print(f"so to tien {n} {a}")
else:
    print("khong hop le")