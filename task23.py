with open("Input/grades.csv") as f:
    f.readline()
    lines = f.read().splitlines()

grades = dict()
for line in lines:
    name, grade = line.split(',')
    if grade not in grades.keys():
        grades[grade] = []
    
    grades[grade].append(name)

with open("Output/output23.txt", "w") as f2:
    f2.write(str(grades))