def extract_person_info(lines):
    for line in lines:
        name_start = line.find("@") + 1
        name_end = line.find("|", name_start)
        name = line[name_start:name_end]

        age_start = line.find("#") + 1
        age_end = line.find("*", age_start)
        age = line[age_start:age_end]

        if name and age:
            print(f"{name} is {age} years old.")


if __name__ == "__main__":
    N = int(input())
    lines = []

    for _ in range(N):
        line = input()
        lines.append(line)

    extract_person_info(lines)
