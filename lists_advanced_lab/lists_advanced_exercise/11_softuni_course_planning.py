courses = input().split(', ')

command = input().split(':')

while not command[0] == 'course start':
    if command[0] == "Add":
        if not command[1] in courses:
            courses.append(command[1])
    if command[0] == "Insert":
        if not command[1] in courses:
            index = int(command[2])
            courses.insert(index, command[1])
    if command[0] == "Remove":
        if command[1] in courses:
            index = courses.index(command[1])
            if index < len(courses) - 1 and courses[index + 1].endswith("-Exercise"):
                del courses[index:index + 2]
            else:
                del courses[index]
    if command[0] == "Swap":
        if command[1] in courses and command[2] in courses:
            index1 = courses.index(command[1])
            index2 = courses.index(command[2])
            courses[index1], courses[index2] = courses[index2], courses[index1]
            if index1 < len(courses) - 1 and courses[index1 + 1].endswith("-Exercise") \
                    and index2 < len(courses) - 1 and courses[index2 + 1].endswith("-Exercise"):
                courses[index1], courses[index1 + 1], courses[index2], courses[index2 + 1] = \
                    courses[index2 + 1], courses[index2], courses[index1 + 1], courses[index1]
            elif index1 < len(courses) - 1 and courses[index1 + 1].endswith("-Exercise"):
                courses[index1], courses[index1 + 1] = courses[index1 + 1], courses[index1]
            elif index2 < len(courses) - 1 and courses[index2 + 1].endswith("-Exercise"):
                courses[index2], courses[index2 + 1] = courses[index2 + 1], courses[index2]
    if command[0] == "Exercise":
        lesson = command[1]
        if lesson in courses:
            index = courses.index(lesson)
            if index == len(courses) - 1 or not courses[index + 1].endswith("-Exercise"):
                courses.insert(index + 1, lesson + "-Exercise")
        else:
            courses.append(lesson)
            courses.append(lesson + "-Exercise")

    command = input().split(':')

# Printing the course schedule
for i, lesson in enumerate(courses, 1):
    print(f"{i}.{lesson}")
