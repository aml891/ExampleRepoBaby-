#This is how we learned to concatenate strings in the ITF+ class
a = "String 1"
b = "String 2"
print("a = " + a + " and b = " + b)

#This syntax utilizes the concept of the f-string
x = "String 3"
y = "String 4"
print(f"x = {x} and y = {y}")

print ("c = {c} and d = {d}".format(c=1, d=2))

job_list = {"John": "Doctor", "Jane": "Engineer", "Jim": "Teacher"}

for name, job in job_list.items():
    print(f"{name} is a {job}")