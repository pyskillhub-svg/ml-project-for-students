# weeknum = int(input("enter week number"))
if weeknum == 0:
    print("sunday")
elif weeknum == 1:
    print("monday")
else:
    print("wrong weeknum enters please enter 0-6!")

# BMI Calculation
'''
BMI<18.5 ---- your under weight
BMI  18.5 to 24.9 ---- your normal weight
BMI 24.9 to 29.9 ---- your over weight
BMI >30 ---- your over obesity
BMI = weight/(height*height)*10000

inputs height, weight
'''
print("Welcome to BMI Calculation")

height = float(input("enter your height in cms"))
weight = float(input("enter your weight in kgs"))

BMI = weight/(height*height)*10000
print("your BMI is ",BMI)
if BMI < 18.5:
    print("your under weight")
elif 18.5<BMI<24.5:
    print("your normal weight")
elif 24.9<BMI<29.9:
    print("your over weight")
else:
    print("your obesity")


# name = "Python", "welcome to bangalore"
# count how many vowels are these

name = input("enter your name")

count = 0
vowels = 'aeiouAEIOU'

for ch in name:
    if ch in vowels:
        count += 1
print(count)


