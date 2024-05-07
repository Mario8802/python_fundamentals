countries = input().split(", ")
capitals = input().split(", ")
# final_information = {countries[index]: capitals[index]
#                      for index in range(len(countries))}
final_information = dict(zip(countries, capitals))
for country, capital in final_information.items():
    print(f"{country} -> {capital}")



# Using a dictionary comprehension,
# write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", ").
# Print each country with their capital on a separate line in the following format: "{country} -> {capital}".


countries = input().split(', ')
cities = input().split(', ')

zip_countries = zip(countries,cities)
my_dictionary_with_countries = dict(zip_countries)

for k,v in my_dictionary_with_countries.items():
    print(f"{k} -> {v}")
