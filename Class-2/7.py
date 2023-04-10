a = ["daniel", "shai, "roei"]
# shortcut for: if a[0] =="shmulik" or a[1] =="shmulik" or a[2]] == "shmulik":
#print ("found shmulik")

if "shmulik" in a:
print("found shmulik")

first_array= []
second_array= [1,2,3]
if not first_array:
    print("first has no items")
if second_array:
    print("second array has items")
if len(second_array) > 2:
    print("we have at least 3 items in second")

d=5
g=5
f=[1,2,3]
h=[1,2,3]
if d is g:
    print("d is g")
if f is h:
    print("f is h")