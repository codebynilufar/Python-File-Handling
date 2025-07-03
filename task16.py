with open("Input/students.txt") as f:
    names = f.read().split()

lines = []
for name in names:
    if len(name) > 5:
        lines.append(f"{name}- 5 harfdan uzun.")

with open("Output/output16.txt", 'w') as f2:
    f2.write("\n".join(lines))


