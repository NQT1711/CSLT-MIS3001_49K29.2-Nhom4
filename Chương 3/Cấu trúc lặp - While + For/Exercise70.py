
message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số lượng ca "))


ketqua = ""


for char in message:
    if char.isalpha():  
        # Xác định trường hợp của chữ cái (chữ hoa hoặc chữ thường)
        is_upper = char.isupper()

        # Chuyển chữ cái theo số lượng được chỉ định
        shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))

        # Nối ký tự đã dịch chuyển vào ketqua
    
        ketqua+= shifted_char
    else:
        # Các ký tự không phải chữ cái không được sửa đổi bởi mật mã
        ketqua+= char

print("Shifted message:", ketqua)