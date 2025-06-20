#14. Write a Python program to find the highest 3 values in a dictionary

my_dict = {'a': 50,'b': 70, 'c': 10, 'd': 40, 'e': 80}

sorted_item = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

top_3 = sorted_item[:3]
print("Top 3 highest value of dictionary: ")
for key, Value in top_3:
    print(f"{key}:{Value}") 