#A garding system programme
#prompt the user to input unit marks
unit1 = int(input("Enter marks for unit 1: "))
unit2 = int(input("Enter marks for unit 2: "))
unit3 = int(input("Enter marks for unit 3: "))
unit4 = int(input("Enter marks for unit 4: "))
#calculate average
average = (unit1+unit2+unit3+unit4)/4
#ues condition statements to append grades
if average >=70 and average <=100:
    print("Grade A.")
elif average >=60 and average<=69:
    print("Grade B.")
elif average >=50 and average<=59:
    print("Grade C.")
elif average >=40 and average<=49:
    print("Grade D")
elif average >=0 and average<=39:
    print("FAIL!")
#print this if the user enters marks less than 0 or over 100
else:
    print("Invalid marks")
