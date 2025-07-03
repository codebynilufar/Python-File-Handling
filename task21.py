with open("Input/grades.csv") as f:
    f.readline()
    lines = f.readlines()

rows = list(map(
    lambda line: line.strip().split(','),
    lines
))

highest_grade = max(
    rows,
    key=lambda row: float(row[1])
)


with open("Output/output21.txt", "w") as f2:
    f2.write(str(highest_grade))