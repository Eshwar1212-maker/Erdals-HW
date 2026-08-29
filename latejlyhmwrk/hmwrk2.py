
from collections import Counter

sentence = input("enter sentence: ")


letters = [char for char in sentence.lower() if char.isalpha()]
letter_counts = Counter(letters)


sorted_words = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

print(sorted_words)

for letter, count in sorted_words:
    print(f"{letter} → {"*" * count}")