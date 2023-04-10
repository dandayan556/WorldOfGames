# 1. input for 5 ages from the user
# 2. print out the biggest age from the user
age1 = int(input("enter your first age: "))
age2 = int(input("enter your second age: "))
age3= int(input("enter your third age: "))
age4 = int(input("enter your fourth age: "))
age5 = int(input("enter your fifth age: "))
if age1>age2 and age1>age3 and age1>age4 and age1>age5:
    print('age1 is oldest')
if age2>age1 and age2>age3 and age2>age4 and age2>age5:
     print('age2 is oldest')
if age3>age1 and age3>age2 and age3>age4 and age3>age5:
    print('age3 is oldest')
if age4 > age1 and age4 > age2 and age4 > age3 and age4>5:
    print('age4 is oldest')
if age5 > age1 and age5 > age2 and age5 > age3 and age5 >age4:
    print('age4 is oldest')

