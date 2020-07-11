# Write a python program which will keep adding a stream of numbers inputted by the user.
# # The adding stops as soon as user presses q key on the keyboard.
import sys
sum = 0
while(True):
    number = input("Enter the item price or press q to quite: \n")
    if number != 'q':
        sum = sum + int(number) 
        print(f"Order total so far : {sum}") 
    else:
        print(f"Your Bill total is {sum}. Thanks for shopping with us!")
        break
