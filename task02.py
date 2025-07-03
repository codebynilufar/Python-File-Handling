f = open("Input/numbers.txt", "r")
numbers = f.readlines()

total = sum(map(int, [n.strip() for n in numbers]))

f.close()

f2 = open("Output/output02.txt", "w")
f2.writelines("Yig'indisi: " + str(total))
f2.close()
