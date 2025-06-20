#6.  Write a Python program to find the first appearance of the substring 'not' and
#    'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#     substring with 'good'. Return the resulting string


word = input("Enter a Senetnce: ")

not_pos = word.find("not")
poor_pos = word.find("poor")

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
    result = word[:not_pos]+ "good"+ word[poor_pos + 4:]

else:
    result = word


print(result)