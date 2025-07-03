with open("Input/students.txt") as f:
    students = f.read().split()

count_students = [f" ismlar soni: {len(students)}"]

with open("Output/output12.txt", "w") as f2:
    f2.write(str(count_students))