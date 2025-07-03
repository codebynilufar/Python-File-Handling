with open("Input/numbers.txt") as f:
    content = f.read()


nums = content.split()
result = list(map(
    lambda num: f"{num} {len(num)} xona ", nums
))

with open("Output/output09.txt", 'w') as f:
    f.write("\n".join(result))
