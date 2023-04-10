#Write the following code: a = 1/0. Build a corresponding try-except block to avoid exception.
if __name__ == '__main__':
    try:
        a = 1 / 0
    except:
        print("Division by zero")