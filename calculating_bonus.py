# program to calculaye bonus
#prompt the user to enter salary
salary = float(input("Input your salary: "))
#prompt the user to enter years of service
years_of_service = float(input("Enter your years of service: "))
#use if condition statement to check how long the employee has stayed to calculate the bonus
if years_of_service >= 10:
    #calculate the bonus
    bonus = (0.1* salary)
    #print the bonus
    print("Bonus =", bonus)
elif years_of_service >=6 and years_of_service <=10:
    bonus = (0.08 * salary)
    print("Bonus =", bonus)
else:
    bonus = (0.05* salary)
    print("Bonus =",bonus)