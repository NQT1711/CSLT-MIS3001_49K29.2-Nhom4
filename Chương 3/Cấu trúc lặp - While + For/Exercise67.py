total_cost = 0

# Đọc tuổi của khách cho đến khi nhập vào dòng trống
while True:
    age_input = input("nhap tuoi khach: ")

    if age_input == "":
        break

    # Chuyển đổi đầu vào thành số nguyên
    try:
        age = int(age_input)
    except ValueError:
        print("khong hop le, xin nhap lai.")
        continue

    # Tính chi phí nhập học theo độ tuổi
    if age <= 2:
        cost = 0
    elif 3 <= age <= 12:
        cost = 14.00
    elif age >= 65:
        cost = 18.00
    else:
        cost = 23.00

    # Cộng chi phí vào tổng
    total_cost += cost

# Hiển thị tổng chi phí nhập học cho nhóm
print(f"\ntong chi phi nhap hoc cho nhom: ${total_cost:.2f}")