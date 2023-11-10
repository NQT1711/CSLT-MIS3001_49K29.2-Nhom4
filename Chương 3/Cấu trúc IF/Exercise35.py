human_years=int(input("Enter the number of human years: "))

if human_years<0:
    print("Please enter a non-negative number!")
elif human_years==1:
    dog_years=10.5
elif human_years==2:
    dog_years=21
else:
    dog_years=21+(human_years-2)*4

if human_years>=0:
    print("The equivalent dog years is:",dog_years)
