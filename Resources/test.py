from collections import Counter

words = []
with open("fileToBeHandled.txt", "r") as file1:
    for line in file1:
        for word in line.split():
            words.append(word)

word_counts = Counter(words)
print("First method using Collections module:\n",word_counts, "\n")

# Alternatively:
word_counts = {}

with open("fileToBeHandled.txt", "r") as file1:
    for line in file1:
        for word in line.split():
            word_counts[word] = word_counts.get(word, 0) +1

print("Second method using dictionary:\n", word_counts, "\n") # One line output, OR:
print("Print by looping through dictionary: ")
for x, y in word_counts.items():
    print(f"Word: {x}, Count: {y}")