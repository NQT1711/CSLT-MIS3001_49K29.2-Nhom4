n = str(input("Tên của một chữ cái: "))
alpha = ["a", "e", "i", "o", "u"]
alphas = ["y"]
if n.lower() in alpha:
    print("Chữ cái", n, "là một nguyên âm")
elif n.lower() in alphas:
    print("Chữ cái", n, "là một nguyên âm, đôi khi là một phụ âm")
else:
    print("Chữ cái", n, "là một phụ âm")
