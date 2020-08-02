import random
num = random.randint(0, 100) # Generates a random number between 1 and 100
num_guess = 1
while(True):    # Keep running the loop until the number is guessed
    print("Guess the number between 1 to 100")
    user = int(input())
    if user > num:
        print("Lower number please!")
    elif user < num:
        print("Higher number please!")
    else:
        print("Congratulations \U0001F389 you guess the number")
        print("You guessed it in" , num_guess , "attempts\n")
        break
    num_guess += 1
