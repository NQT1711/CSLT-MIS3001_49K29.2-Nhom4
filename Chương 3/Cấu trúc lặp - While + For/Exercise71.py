x = int(input("Nhập số:"))
guess = x/2
error = 0.000000000001
a = 0
while abs((guess**2)-x) > error:
       guess = (guess + x/guess) / 2
       a = a + 1
print(guess)