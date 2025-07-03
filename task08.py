with open("Input/numbers.txt") as f:
    numbers = f.read().split()

s = [int (n) for n in numbers if int(n) % 5 == 0]

with open("Output/output08.txt", 'w') as f2:
      f2.write("\n".join(map(str, s)))
