import string

while True:
    sentence=input("Enter a sentence ('q' to quit): ")

    if sentence=='q':
        break

    modified_sentence=sentence.replace(" ","").translate(str.maketrans("","",string.punctuation)).lower()

    palindrome=modified_sentence==modified_sentence[::-1]

    if palindrome:
        print(f"'{sentence}' is a palindrome")
    else:
        print(f"'{sentence}' is not a palindrome")
