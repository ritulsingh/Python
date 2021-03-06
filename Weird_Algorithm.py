# Consider an algorithm that takes as input a positive integer n.
# If n is even, the algorithm divides it by two, and if n is odd, 
# the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one.
# For example, the sequence for n=3 is as follows:

#                3→10→5→16→8→4→2→1

number = int(input())
print(number)
while (number != 1):
    if (number % 2 == 0):
        number = number // 2
    else:
        number = (number * 3) + 1
    print(number, end=" ")