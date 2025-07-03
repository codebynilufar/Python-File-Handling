count = 0

with open("Input/grades.csv", encoding="utf-8") as f:
    lines = f.readlines()[1:] 

    for line in lines:
        name, grade = line.strip().split(",")
        if int(grade) == 5:
            count += 1

with open("Output/output22.txt", "w", encoding="utf-8") as f2:
    f2.write(f"Bahosi 5 bo‘lganlar soni: {count}")
