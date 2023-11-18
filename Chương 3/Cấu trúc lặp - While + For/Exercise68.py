while True:
    # Đọc 8 bit từ người dùng
    bit = input("Nhập 8 bit:")
    if bit == "":
        break

    # Kiểm tra xem đầu vào có chứa chính xác 8 bit không
    if len(bit) != 8 or not bit.isdigit():
        print("loi.")
        continue

    # Đếm số bit một trong đầu vào
    so = bit.count('1')

    # Xác định bit chẵn lẻ (0 cho chẵn lẻ, 1 cho chẵn lẻ lẻ)
    chan_le = 0 if so % 2 == 0 else 1

    print(f"Bit chan le: {chan_le}")