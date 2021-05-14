"""
this allows the user to input students
then it calculates the percentage then they can input if the student is presnet
and at the end it shows the list of present studens at the end of the program with the percentage
"""
import math

if input("add students? [y/n]").lower().strip()=="y":
    names = []
    while True:
        new_name = input("names: ")
        if new_name=="exit": break
        else:
            names.append(new_name.strip())

else:
    names = ["bob", "jack", "mark", "brown", "kali", "what"]
list_absent = []
liat_present = []
name_absent = 0
name_present = 0
per_add = (100 / len(names))
per_add = math.trunc(per_add)

print(names)

for student in names:
    if len(student)<=0:
        continue
    else:
        print(student)
        if input("is student here [y/n]").lower()=="y":
            liat_present.append(student)
            name_present += per_add
        else:
            list_absent.append(student)
            name_absent += per_add


while True:
    if name_absent + name_present >=100:
        break
    if name_absent + name_present <100:
        if name_absent<=name_absent:
            name_absent += 1
        else:
            name_absent += 1

for i in liat_present:
    print(f"student: {i}")
print(f"present %{name_present}\ny")
for i in list_absent:
    print(f"student: {i}")
print(f"present %{name_absent}\n")

while True:
    if input()=="y":
        break
