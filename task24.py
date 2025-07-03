with open("Input/grades.csv") as f:
    lines = f.readlines()[1:]  

grades = [int(line.strip().split(",")[1]) for line in lines]
average = sum(grades) / len(grades)

above = [line.strip().split(",")[0] for line in lines if int(line.strip().split(",")[1]) > average]


with open("Output/output24.txt", "w") as f2:
    f2.write("\n".join(above))
