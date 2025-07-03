with open("Input/students.txt") as f:
    students = f.read().split()

students.reverse()

with open("Output/output14.txt", "w") as f2:
    f2.write(str(students))