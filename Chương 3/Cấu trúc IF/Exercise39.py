n = float(input("nhap muc am thanh: "))

if n < 0:
    print("vui long nhap so duong.")
elif n < 40:
    print("Muc am thanh yen tinh hơn phong yen tinh.")
elif n == 40:
    print("Muc am thanh phu hop phong yen tinh.")
elif n < 70:
    print("muc am thanh nam giua phong yen tinh and dong ho bao thuc.")
elif n == 70:
    print("muc am thanh phu hop dong ho bao thuc.")
elif n < 106:
    print("muc am thanh nam giua dong ho bao thuc and may cat co.")
elif n == 106:
    print("muc am thanh phu hop may cat co.")
elif n < 130:
    print("muc am thanh nam giua may cat co and bua khoan.")
elif n == 130:
    print("muc am thanh phu hop  bua khoan.")
else:
    print("Muc am thanh to hơn  bua khoan.")