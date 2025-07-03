with open("Input/numbers.txt") as f:
    content = f.read()

nums = content.split()
max_number = max(nums, key=int)

with open("Output/output03.txt", 'w') as f:
    f.write(f"Max: {max_number}")
