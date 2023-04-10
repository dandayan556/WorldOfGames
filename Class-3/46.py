def get_age():
    current_age = int(input("enter your age: "))
    if current_age < 0:
        raise BaseException("age can not be negative", current_age)


try:
    get_age()
except BaseException as e:
    print(e.args)