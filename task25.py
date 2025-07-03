with open("Input/grades.csv") as f:
    lines = f.readlines()[1:] 


five_students = [line.strip().split(",")[0] for line in lines if int(line.strip().split(",")[1]) == 5]


with open("Output/output25.txt", "w") as f2:
    f2.write("\n".join(five_students))
