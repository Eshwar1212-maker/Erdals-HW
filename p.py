from collections import Counter

sentence = "Hello, World!"

# Filter for letters only and convert to lowercase
letters = [char for char in sentence.lower() if char.isalpha()]
letter_counts = Counter(letters)

print(letter_counts)  
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
