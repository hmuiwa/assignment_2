# Accepts user input and calculates the sum of integers in the list
integers = input("Enter a list of integers separated by spaces: ").split()
integers = [int(num) for num in integers]  # Convert input strings to integers
print(f"The sum of the integers is: {sum(integers)}")






