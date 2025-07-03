with open("Input/numbers.txt") as f:
    nums = [int (x) for x in f.read().split()]

square = [n ** 2  for n in nums ]

with open("Output/output07.txt", 'w') as f2:
    f2.write(" ".join(map(str, square)))