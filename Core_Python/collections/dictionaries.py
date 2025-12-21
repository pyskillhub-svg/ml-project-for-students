'''
dictionaries are key-value pair collection
we can represent in {}
we can use dict keyword for dictionary creation
keys are unique, values may duplicate.
dictionaries are mutable.
'''

# creating empty dictionary
d1 = {}
print(type(d1))

# creating dictionary ; same key name and updated repeatedly
# student_result = {'Neel':'3rd class','Neel':'2nd class'}

# adding methods in dictionary , = , update methods
countries_capitals = {'India':'Delhi','China':'Beijing','US':'Pentagon','UK':'London'}
countries_capitals['srilanka'] = 'colombo'
print(countries_capitals)
# update method


# we can use for loop for reading of dictionary
# for i in countries_capitals: # we will get only keys
#     print(i)
#
# for i in countries_capitals: # values only
#     print(countries_capitals[i])

# for i in countries_capitals.keys():
#     print(i)
# for j in countries_capitals.values():
#     print(j)
# for i,j in countries_capitals.items():
#     print(i,j)

# membership operators in , not in
# if 'India' in countries_capitals:
#     print("exist")
# else:
#     print("not exist")
# different between get and normal checking method
# print(countries_capitals.get('Germary'))
# print(countries_capitals['Germany']) # directly accesing key -value

# deleting items from the dictionary

# pop(): key must be pass, it will removed passed key-valu pair
countries_capitals.pop('UK')
print(countries_capitals)

# popitem() never take any key, by default removed last item
countries_capitals.popitem()
print(countries_capitals)

# clear() :
# del if we pass key, it will removed that pair , if we can pass dictionary it will removed entire dictionary
# del countries_capitals['China']
# print(countries_capitals)

# del countries_capitals

# countries_capitals_latest = countries_capitals.copy()

# fromkeys(), setdefault()
# students = ['neel','ronald','shambhu','prasad','vijay']
# results = ['pass']
# my_college_result = dict.fromkeys(students,results)
# print(my_college_result) # list, compression, dictionary compression, set compression
# print(my_college_result['neel'])
#
# my_college_result.setdefault('neel','fail') # if the key already have a value that value will be there,not changed, if the key not there this pair will be added to that dicitonary
#
# print(my_college_result)

countries_capital = {'India':'Delhi','China':'Beijing','US':'Pentagon','UK':'London'}

countries_capital.setdefault('Indian','New Delhi')
print(countries_capital)

# Nested dictionaries
my_institute = {"stu1":
                    {'name':'Neel','course':'AI'},
                "stu2":
                    {'name':'Ronald','course':'ML'},
                "stu3":
                    {'name':'Shambhu','course':'Python Developer'}
                }
print(my_institute['stu3']['course'])
print(my_institute['stu1'])