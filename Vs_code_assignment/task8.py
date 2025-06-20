#8. Write a Python program to check whether a list contains a sublist.


def is_sublist(main_list, sub_list):
    n = len(sub_list)
    for i in range(len(main_list) - n +1):
        if main_list[i:i+n] == sub_list:
            return True
        else:
            return False
        
 
main_list = [3,4]
sub_list = [3,4]
if is_sublist(main_list, sub_list):
    print("sub list founded")

else:
    print("sub list is not founded")


