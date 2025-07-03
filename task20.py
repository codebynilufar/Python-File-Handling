with open("Input/grades.csv") as f:
    grades = [int(line.split(',')[1])         
              for line in f.readlines()[1:]]  

average = sum(grades) / len(grades)

with open("Output/output20.txt", "w") as f2:
    f2.write(f"O'rtacha baho: {average:.2f}")
