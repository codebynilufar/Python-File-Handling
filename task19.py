with open("Input/grades.csv") as f:
    names = f.read().split()


with open("Output/output19.txt", "w") as f2:
    f2.write("\n".join(names))