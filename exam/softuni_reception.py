first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

counter = 0
needed_time =0

time_per_hour =  int(first_employee + second_employee + third_employee)
while students_count > 0:
    students_count -= time_per_hour
    needed_time += 1

    if (needed_time - counter) % 3 == 0:
        needed_time += 1
        counter += 1

print(f'Time needed: {needed_time}h.')