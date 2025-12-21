'''
1.by default return will give None
2.if we can write any no of returns only one execution will be happen
3.once return will execute that function will be terminated
4.we can write multiple return statements but only one execution will be happen
5. return will give you multiple values
'''
# no return value
def wish(name):
    return

print(wish('siva'))
# multiple returns
def greetings(name):
    return f"Good morning {name}"
    return f"good afternoon {name}"
print(greetings('Neel'))

# condition based return statements
def even_no(num):
    if num%2 ==0:
        return " this is even no"
    return "this is odd no"
print(even_no(5))

#return will give you multiple values

def marks_info(marks):
    total = sum(marks)
    average = total/len(marks)
    return average,total
data = [56,47,86,78,88,67]
student_grade,student_average = marks_info(data)
print(f" student total marks is {student_grade}student average marks is {student_average}")













