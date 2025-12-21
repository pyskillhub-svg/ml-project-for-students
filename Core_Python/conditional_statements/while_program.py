"""
syntax
initialion
while condition:
    statements
    increment/decrement mondatory
"""

i =1
while i <6:
    print(i)
    i = i+1
print("end of the program")

'''
softkeywords
'''

# match, case, _ program

# WAP to book movie tickets for different category

'''
match initilization:
    case condtion:
        statements
    case condtion:
        statements
    case _:
        statement
        3.10 onwards available these softkeys
'''

class_type = input("please enter class type ['Diamond'','Gold','Silver'] for ticket booking")

match class_type:
    case "Diamond":
        print("Book the Diamond class ticket")
    case _:
        print("Please select the available class_type")


