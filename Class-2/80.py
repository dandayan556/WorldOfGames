total = 0
i=0
while i<5:
    age=int(input())
    i+=1
    if age<3:
        continue
    total+=100
print(total)