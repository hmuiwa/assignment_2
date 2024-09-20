# List of words
words = ["apple", "banana", "grape", "orange", "plum", "kiwi"]

# List comprehension to create a new list with words having odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print(f"Words with an odd number of characters: {odd_length_words}")
