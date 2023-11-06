course_dict = {}
course = ''

while True:
    command = input()

    if command == 'end':
        break
    command = command.split(' : ')
    course = command[0]
    student_name = command[1]

    if course not in course_dict:
        course_dict[course] = []

    course_dict[course].append(student_name)

for courses in course_dict:
    print(f'{courses}: {len(course_dict[courses])}')

    for student in course_dict[courses]:
        print(f'-- {student}')