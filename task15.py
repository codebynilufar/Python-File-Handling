with open("Input/students.txt", encoding="utf-8") as f:
    names = f.read().split()

lines = []
for name in names:
    lines.append(f"{name} — {len(name)} harf")


with open("Output/output15.txt", "w", encoding="utf-8") as f2:
    f2.write("\n".join(lines))
