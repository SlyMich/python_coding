# Prompt the user to enter citizenship
citizenship = input("Enter citizenship:")
# Prompt the user to inputt Age in years
age = int (input("Enter your age:"))
# Test validity of citizenship and Age using logical and assignment operators
if  age >= 18 and citizenship.lower() == "kenyan":
    # Display this if the condition is met
    print ("You are eligible to vote?")
else:
    # Display this if condition is not met
    print("You can't vote.")
