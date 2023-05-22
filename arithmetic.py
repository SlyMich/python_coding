#prompt the user to input the amount
purchase = float (input("amount:"))
#comparison operator
if purchase > 1000:
    print("A discount of 5 percent is given")
    #calculating the discount
    discount = purchase*0.05
    #calculating the final amount after discount
    finalAmount = purchase - discount 
    #display the discount
    print("Discount", discount)
   #display the final amount
    print("Final amount", finalAmount)
else:
    print(" no discount")