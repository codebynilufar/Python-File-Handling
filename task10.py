with open("Input/numbers.txt") as f:
    numbers = f.read().split()
nums = [int(n) for n in numbers]
nums.sort()

with open("Output/output10.txt", "w") as f2:
    f2.write("\n".join(map(str, nums)))