# Prompt the user to input income
Income= int(input ("Input your income:"))
#Use relational/comparison operator to set required minimum limit for income 
if Income >= 21000:
# Prompt the user to input Age
    Age = int (input("Enter your age in years:"))
    # Use relational/comparison operator to set required minimum Age
    if Age >= 21:
        # Display this if condition of age and income is met
        print("Congratulations, you qualify for a loan!")  
    else:
        # Display this if condition of age is not met
        print("Unfortunately we are unable to offer you a loan at this time.")
else:
    # Display this if condition of income is not met
     print("Unfortunately we are unable to offer you a loan at this time.") 