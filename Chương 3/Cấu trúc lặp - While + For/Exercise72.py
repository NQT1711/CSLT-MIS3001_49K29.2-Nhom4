line=input("Enter a string: ")
palindrome=True

for i in range(0,len(line)//2):
    if line[i]!=line[len(line)-i-1]:
        palidrome=False

if palindrome:
    print(line,"is a palindrome")
else:
    print(line,"is not a palindrome")
