# Accept user input to create two sets of integers
set1 = set(map(int, input("Enter integers for the first set (separated by spaces): ").split()))
set2 = set(map(int, input("Enter integers for the second set (separated by spaces): ").split()))

# Create a new set with elements common to both sets
common_elements = set1.intersection(set2)

print(f"The common elements are: {common_elements}")
