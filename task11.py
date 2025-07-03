with open("Input/students.txt") as f:
    students = f.read().split()

with open("Output/output11.txt", "w") as f2:
    f2.write(str(students))