import random
import string


class User:
    def __init__(self, user_id,name,password):
        self.details = (user_id,name,password)

    def user_id(self):
        print(f"User ID: {self.details[0]}\nName: {self.details[1]}\nPassword: {self.details[2]}")

def generator_pass(user_input):
    try:
        if len(user_input) < 3:
            raise ValueError("Input must be atleast 3 character of generate password")
        
        has_letter = any(char.isalpha() for char in user_input)
        has_digit = any(char.isdigit()for char in user_input)
        has_symbol = any(char in "!@#$%^&*" for char in user_input)

        if not (has_letter and has_digit and has_symbol):
            raise Exception("Password Generation Failed.\nPlease Enter Letter, Digits and Symbol.")
        
        chosen_char = ''.join(random.choices(user_input,k=5))
        digits = ''.join(random.choices(string.digits,k=4))
        symbol = ''.join(random.choices("!@#$%^&*",k=1))
        upper = ''.join(random.choices(string.ascii_uppercase,k=1))
        password = chosen_char+digits+symbol+upper
        password = ''.join(random.sample(password,len(password)))

        if len(password)< 8:
            raise Exception("Password generation Failed.\nGenerated Password too short.")
        
        return password
    
    except Exception as e:
        print("Error",e)
        return None
    

users = []
while True:
    try:
        user_id = int(input("Enter Your User ID in (numeric): "))
        name = input("Enter Your Name: ")
        user_input = input("Please Enter Letter, Digits and Symbol for Password: ")
        
        password = generator_pass(user_input)

        if password:
            user = User(user_id,name,password)
            users.append(user)
            print("User Created Successfully!!\n")

        more = input("Add another user? yes/no: ").lower()
        if more != 'yes':
            print("Thank You")
            break

    except ValueError:
        print("Invalid Input! Please Enter correct data types.\n")
    
    except Exception as e:
        print("Unexpected Error:",e)
