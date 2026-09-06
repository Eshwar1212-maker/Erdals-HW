
sentence = input("Enter a sentence: ").lower()


words = sentence.split()


word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=[True])

print(sorted_words)

#Ask the user to type a sentence. Count how many times each word appears and store it in a dictionary. Print the results sorted from most to least frequent.

#Hints:

#Use .split() to break the sentence into words
#Use .lower() to make it case-insensitive
#Use word_count[word] = word_count.get(word, 0) + 1 to count
#Use sorted() with key=lambda x: x[1], reverse=True to sort
#Expected Output:

#Enter a sentence: the cat sat on the mat the cat sat

#--- Word Frequencies ---
#the → 3
#33cat → 2
#sat → 2
#on → 1
#mat → 1
