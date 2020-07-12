# You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.
# The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).
# Input -> The first input line contains an integer n.
# Output -> Print the missing number.

def getMissingNo(numberList): 
    n = len(numberList) 
    total = (n + 1)*(n + 2)/2
    sum_of_numberList = sum(numberList) 
    return total - sum_of_numberList

n = int(input())
numList = list(int(num) for num in input().strip().split())[:n-1]
miss = getMissingNo(numList) 
print(int(miss)) 
