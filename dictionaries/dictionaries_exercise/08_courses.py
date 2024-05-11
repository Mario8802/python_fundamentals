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

===============================================================================

class CourseRegistration:
    def __init__(self):
        self.courses = {}

    def process_commands(self):
        command = input()
        while command != "end":
            course_name, student_name = command.split(' : ')
            if course_name not in self.courses:
                self.courses[course_name] = []
            self.courses[course_name].append(student_name)
            command = input()

    def print_course_information(self):
        for course_name, registered_students in self.courses.items():
            print(f"{course_name}: {len(registered_students)}")
            for student_name in registered_students:
                print(f"-- {student_name}")


course_registration = CourseRegistration()
course_registration.process_commands()
course_registration.print_course_information()


=============================================================================

courses = {}
command = input()

while command != "end":
    course_name, student_name = command.split(' : ')
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    command = input()

for course_name, registered_students in courses.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")
