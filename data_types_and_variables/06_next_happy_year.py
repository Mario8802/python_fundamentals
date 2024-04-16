year = int(input())
happy_year_condition = False

while not happy_year_condition:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year_condition = len(set_year) == len(str(year))

print(year)


=======================================================================
year = int(input())
is_happy_year = False


while not is_happy_year:
    year += 1
    str_year = str(year)
    set_year = set(str_year)  # easy way
    # for i in range(len(str_year)):  #  
    #     set_year.add(str_year[i])

    is_happy_year = len(str_year) == len(set_year)

print(year)

========================================================================

year = int(input())
while len(set(str(year + 1))) != len(str(year + 1)): year += 1
print(year + 1)


========================================================================


year = int(input())

while True:
    year += 1
    digits = []
    temp_year = year
    while temp_year > 0:
        digit = temp_year % 10
        if digit in digits:
            break
        digits.append(digit)
        temp_year //= 10

    if len(digits) == len(str(year)):
        break

print(year)
