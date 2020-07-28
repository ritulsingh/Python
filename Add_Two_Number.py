# Shivam is the youngest programmer in the world, he is just 12 years old. Shivam is learning programming and today he is writing his first program.

# Program is very simple, Given two integers A and B, write a program to add these two numbers.

# Input
# The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two Integers A and B.

# Output
# For each test case, add A and B and display it in a new line.

# Example
# Input
# 3 
# 1 2
# 100 200
# 10 40

# Output
# 3
# 300
# 50

number_testcase = int(input())
for i in range(1,number_testcase + 1):
    num1, num2 = input().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)