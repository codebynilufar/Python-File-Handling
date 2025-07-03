with open("Input/numbers.txt") as f:
    nums = [int (x) for x in f.read().split()]

odd_number = [n for n in nums if n % 2 == 1]

with open("Output/output06.txt", 'w') as f2:
    f2.write(" ".join(map(str, odd_number)))