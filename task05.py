with open("Input/numbers.txt") as f:
    nums = [int(x) for x in f.read().split()]

total = sum([n for n in nums])
average = total / len(nums)

with open("Output/output05.txt", "w") as f2:
    f2.write(f"average: {average}")