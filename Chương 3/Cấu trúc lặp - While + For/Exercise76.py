nguoi_dung = input("nhap so nguyen lon hon hoac bang 2: ")

so = int(nguoi_dung)
if so < 2:
    print("loi, nhap so nguyen lon hon hoac bang 2.")
else:
    print(f"so nguyen to cua {so}:")
    nhan_to = 2
    while nhan_to <= so:
        if so % nhan_to == 0:
            print(nhan_to)
            so //= nhan_to
        else:
            nhan_to += 1
