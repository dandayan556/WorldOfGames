def get_name():
    current_name = input("enter your name: ")
    my_file = open("names.txt", "a")
    my_file.write(f"{current_name}\n")
    my_file.close()

with open("names.txt") as my_file:
    for line in my_file.readlines():
        print(line)


def show_names():
    my_file = open("names.txt")
    for line in my_file.readlines():
        print(f"hello {line}", end='')
    my_file.close()


for i in range(3):
    get_name()
show_names()