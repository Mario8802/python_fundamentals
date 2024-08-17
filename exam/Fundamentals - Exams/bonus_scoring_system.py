import math
import sys

students = int(input())
lectures = int(input())
bonus = int(input())

bonus_for_print = 0
max_lectures = 0

for _ in range(students):
    attendances = int(input())
    if lectures > 0:
        total_bonus = (attendances / lectures) * (5 + bonus)
    else:
        total_bonus = 0

    if total_bonus > bonus_for_print:
        bonus_for_print = total_bonus
        max_lectures = attendances

print(f"Max Bonus: {math.ceil(bonus_for_print)}.")
print(f"The student has attended {max_lectures} lectures.")
