# Prompt the user to input nationality
Nationality = str(input("Enter Nationality:"))
# Test the eligibility by nationality
if  Nationality.lower()== "kenyan":
# Prompt the user to input age
    Age = int (input("Enter your age in years:"))
# Relational/comparison operator to set age minimum limit
    if  Age >= 18:
# Display this if condition of age is met
        print("Proceed to vote.")
    else:
# Display this if age condition is not met
        print("You are too young to vote.")
else:
# Display this if Nationality condition is not met
    
  print("You should be a Kenyan to be allowed to vote.")  
 