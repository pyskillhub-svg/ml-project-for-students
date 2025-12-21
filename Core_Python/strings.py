'''
strings are immutable
strings follow index
strings following slice operator
strings have format options
we can use str() for creating string. str(2), str(hi)
we can use single quotes, doublel quotes or trible quotes for string creation purpose
even space also will consider and counted in strings. 'hi '
'''
# empty string creation
s1 = ''
s2 = ""
s3 = ''' '''
s4 = """ """
# creating string
s5 = 'python'
# indexing in strings
# print(s5[0]) # p
# print(s5[-1]) # n

# slicing in strings
# print(s5[0:3:2])
# print(s5[-1:-5:-2])
# mathematical operations in strings + concatination,* repetation
# s6 = 'python'
# s7 = 'is language'
# print(s6+s7)
# print(s6*3)

# methods in strings, upper(),lower(),capitalize(),title()
# str1 = 'Python Is dynamic programming language'
# print(str1.upper())
# print(str1.lower())
# print(str1.capitalize()) # starting letter only capitalize remaining all small letters
# print(str1.title())

# space remove methods
# str2 = "   python  "
# print(str2.lstrip())
# print(str2.rstrip())
# print(str2.strip())

# searching of strings find, index, count, startswith, endswith
#
# str1 = 'python is a programming language'
# print(str1.find('u'))
# print(str1.index('i'))
# print(str1.count('a'))

# replace method
# print(str1.replace('an','easy'))
#
# movies_list = ['Bhabubali','Krish','Bhadra','rebel']
# for movie in movies_list:
#     if movie.startswith(('K','B')):
#         print(movie)
# endswith we can try

# string checking methods isalpha(),isdigit(),isalnum(),isspace(),isupper(),islower()
str2 = 'Python123 '
# print(str2.isspace())
# print(str2.istitle())
# print(str2.islower())
# print(str2.isupper())
# print(str2.isdigit())
# print(str2.isalnum())

# escape characters
# str3 = "hello\\world"
# print(str3)
# # \t, \\, 'string\'string\''
# str4 = 'hello\'world\''
# print(str4)

# comparison methods and membership operations will support strings
s1 = 'apple'
s2 = 'berry'
print(s1 == s2)
print(s1>s2)
print(s1<s2)
a = 'A'
print(ord(a))
print('a' in s1)

# alignment methods

s5 = 'python'
print(s5.center(25))
print(s5.ljust(30))
print(s5.rjust(10))














