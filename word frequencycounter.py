text = input("Enter a passage: ")

# Convert to lowercase and split into words
words = text.lower().split()

# Count word frequencies using a dictionary
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

# Sort words by frequency in descending order
top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Display top 5 frequent words using list comprehension
result = [f"{word}: {count}" for word, count in top_words[:5]]

print("\nTop 5 Most Frequent Words:")
for item in result:
    print(item)