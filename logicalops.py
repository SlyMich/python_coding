citizenship = input("Enter citizenship:")
age = int (input("Enter your age:"))
if  age >= 18 and citizenship.lower() == "kenyan":
    print ("You are eligible to vote?")
else:
    print("You can't vote.")