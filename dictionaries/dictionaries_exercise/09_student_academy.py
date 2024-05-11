the_next_pair_of_rows = int(input())
final_dictonary = {}

for i in range(the_next_pair_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in final_dictonary:
        final_dictonary[student_name] = []

    final_dictonary[student_name].append(grade)

for student, grade in final_dictonary.items():
    sum_grades = 0

    for current_grade in grade:
        sum_grades += current_grade
    avg_grade = sum_grades / len(grade)

    if avg_grade >= 4.50:
        print(f'{student} -> {avg_grade:.2f}')



==============================================================================




n = int(input())
student_data = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in student_data:
        student_data[student] = [grade, 1]
    else:
        student_data[student][0] += grade
        student_data[student][1] += 1

for student, data in student_data.items():
    sum_grades, num_grades = data
    average_grade = sum_grades / num_grades
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
