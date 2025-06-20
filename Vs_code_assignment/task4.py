 #4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

str1 = input("Enter a first sentence: ")
str2 = input("Enter a second sentence: ")

first2_str1 = str1[:2]
first2_str2 = str2[:2]

remain1_str1 = str1[2:]
remain2_str2 = str2[2:]

new_str1 = first2_str2 + remain1_str1
new_str2 = first2_str1 + remain2_str2

result = new_str1 + " " +new_str2
print(remain1_str1, remain2_str2)
print(result)
