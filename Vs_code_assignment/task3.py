#3. Write a Python program to count the occurrences of each word in a given sentence.

sentence = input("Enter a Sentence: ")

words =  sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1

    else:
        word_count[word] = 1


for word in word_count:
    print(word, ":",word_count[word])