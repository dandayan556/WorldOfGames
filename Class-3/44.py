result = 0
try:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    result = a / b
    f = open("kjsndflknsdf.txt")
except ZeroDivisionError as e:
    print("could not divide by zero")
    print(e.args)
except FileNotFoundError:
    print("could not find file")
except BaseException as e:
    print("something went wrong ")
    print(e.args)
print("aviel")