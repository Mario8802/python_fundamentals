number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0


for current_snowball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > max_value:
        max_weight = current_weight
        max_time = current_time
        max_quality = current_quality
        max_value = current_value
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")




n = int(input())

snowball_value = - 1
snowball_weight = - 1
snowball_time = - 1
snowball_quality = - 1

for _ in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    ball = (weight / time) ** quality
    if ball > snowball_value:
        snowball_value = ball
        snowball_quality = quality
        snowball_weight = weight
        snowball_time = time

print(f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})")
