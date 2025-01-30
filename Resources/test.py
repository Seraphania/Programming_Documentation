import re

with open("fileToBeHandled.txt", "r") as file1:
    words = set()
    for line in file1:
        for word in line.split():
            words.add(word)
    for i in words:
        count = re.findall("i", file1)
        print(f"Word: {i}, Count: {count}")