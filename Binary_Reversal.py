# Have the function BinaryReversal(str) take the str parameter being passed,
# which will be a positive integer, take its binary representation (padded to the nearest N * 8 bits),
# reverse that string of bits, and then finally return the new reversed string in decimal form.
# For example: if str is "47" then the binary version of this integer is 101111 but 
# we pad it to be 00101111. Your program should reverse this binary string which then becomes: 11110100 
# and then finally return the decimal version of this string, which is 244.

# Function to convert decimal to binary number
def decimalToBinary(n):  
    return format(n , '08b')

# Function to reverse the binary number 
def reverse(string): 
    string = string[::-1] 
    return string

# Function to convert binary to decimal number 
def binaryToDecimal(n): 
    return int(n,2)

# Driver code 
if __name__ == '__main__':
    n = int(input("Enter the number:\n> "))
    binary = decimalToBinary(n)
    print("Binary number:\n> " + binary)
    reverseBinary = reverse(binary)
    print("Reverse the binary number:\n> " + reverseBinary)
    decimal = binaryToDecimal(reverseBinary)
    print("Again convert the reverse binary to decimal number:\n>",decimal)