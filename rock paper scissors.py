import random

def guess(you, comp):
    if(you == comp):
        return 0
    if you=='r' and comp=='s':
        return -1
    elif you=='s' and comp=='r':
        return 1
    if you=='r' and comp=='p' :
        return 1
    elif you=='p' and comp=='r':
        return -1
    if you=='s' and comp=='p' :
        return -1
    elif you=='p' and comp=='s' :
        return 1
if __name__ == "__main__":
    rand_num = random.randint(1, 100)
    if rand_num < 33 :
        comp = 'r'
    elif rand_num > 33 and rand_num < 66 :
        comp='p'
    else:
        comp='s'
    print("Rock paper scissors is a hand game usually played between two people but you can not defeat the computer!")
    print("----------------------------------------------------------------------------------------")
    print("For \"rock\" enter \"r\" , For \"paper\" enter \"p\" and For \"scissors\" enter \"s\"")
    you = input()
    result = guess(you, comp)
    if result ==0:
        print("Game draw!\n")
    elif result==1 :
        print("You win!\n")
    else:
        print("You Lose!\n")
    print("You chose", you ,"and computer chose ", comp)
    print(comp)
    print(rand_num)