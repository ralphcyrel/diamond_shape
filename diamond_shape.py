#This code will make a diamond shape
def print_diamond(n):
#Check if n is odd
    if n % 2 == 0:
        print("Input must be an integer" )
        return

#Calculate the middle point
    mid = n // 2
#Upper part of the diamond
    for i in range(mid + 1):
        print(" " * (mid - i) + "*" * (2 * i + 1))
#Lower part of the diamond
    for i in range(mid - 1, -1, -1):
        print(" " * (mid - i) + "*" * (2 * i + 1))
#Example usage of 5
print_diamond(5)
