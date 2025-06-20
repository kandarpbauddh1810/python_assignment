#19. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
    l1 = []
    l2 = []
    for i in l:
        if i not in l1:
            l1.append(i)

        else:
            l2.append(i)
    return l1,l2

original_list = [1,2,3,1,2]
unique_element,duplicate = unique_list(original_list)
print("Original list: ",original_list)
print("Duplicate list: ",duplicate)
print("Unique List: ",unique_element)