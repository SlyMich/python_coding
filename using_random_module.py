#declare a winning number
import random
winning_number = random.randint(1,50)
#prompt the user to guess any number 
user_guessed=int(input("Enter any number: "))
#condition to compare if the guessed number is equal to the winning number the user wins
if  user_guessed == winning_number:
    print("YOU WIN!!")
    #condition to compare if the guessed number is higher than the winning number.

elif user_guessed > winning_number:
    
    print("Too high, guess again.")
else:
    print("Too low, try again.")
    


