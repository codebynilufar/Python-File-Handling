with open("Input/numbers.txt") as f:
    nums = [int (x) for x in f.read().split()]

even_nums = [n for n in nums if n % 2 == 0]

with open("Output/output04.txt", "w") as f2:
    
    f2.write(" ".join(map(str, even_nums)))

