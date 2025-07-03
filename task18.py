with open("Input/students.txt", "r") as f, open("output/output18.txt", "w") as f2:
    names = list(map(str.title, f.read().split()))
    your_name = input("Ismingizni kiriting: ").strip().title()

    if your_name in names:
        f2.write(f"{your_name} ismi mavjud")
    else:
        f2.write(f"{your_name} ismi mavjud emas")
