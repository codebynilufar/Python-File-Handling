with open("input/students.txt") as f:
    names = f.read().split()

lines = []
for name in names:
    if name.lower().startswith("a"):
        lines.append(name)

with open("Output/output17.txt", "w") as f2:
    f2.write("\n".join(lines))