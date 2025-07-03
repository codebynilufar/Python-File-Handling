f = open("Input/numbers.txt", "r")
numbers = f.readlines()

f2 = open("Output/output01.txt", "w")
f2.writelines(numbers)