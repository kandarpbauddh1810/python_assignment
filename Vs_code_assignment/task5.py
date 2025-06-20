#5.  Write a Python program to add 'ing' at the end of a given string (length should be atleast 3). If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged


word = input("Enter A Word: ")

if len(word) < 3:
    result = word

elif word.endswith("ing"):
    result = word + "ly"

else:
    result = word + "ing"

print(result)