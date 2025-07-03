f = open("Input/students.txt", "r")
names = f.readlines()

names.sort()

f2 = open("Output/output13.txt", "w")
f2.writelines(names)