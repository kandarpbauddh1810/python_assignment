from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h = 0
for i in range(75):
    color(hsv_to_rgb(h,1,1))
    h += 0.014
    left(1)
    forward(1)
    for j in range(2):
        left(2)
        circle(140)
    hideturtle()
done()













# #3. Write a Python program to count the occurrences of each word in a given sentence.

# sentence = input("Enter a Sentence: ")

# words =  sentence.split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1

#     else:
#         word_count[word] = 1


# for word in word_count:
#     print(word, ":",word_count[word])