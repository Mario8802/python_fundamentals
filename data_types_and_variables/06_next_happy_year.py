year = int(input())
happy_year_condition = False

while not happy_year_condition:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year_condition = len(set_year) == len(str(year))

print(year)

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
