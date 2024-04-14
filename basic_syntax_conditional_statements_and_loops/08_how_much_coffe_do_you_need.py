# action = input()
 
# coffees = 0
 
# action_to_lower = ['coding', 'movie', 'dog', 'cat']
# action_to_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']
 
# while action != 'END':
 
#     if action in action_to_lower:
#         coffees += 1
#     elif action in action_to_upper:
#         coffees += 2
 
#     action = input()
 
#     if action == 'END':
#         if coffees > 5:
#             print('You need extra sleep')
#         else:
#             print(coffees)

-----------------------------------------------------------------
def count_coffees():
    coffee = 0

    while True:
        command = input()

        if command == "END":
            break

        coffee += evaluate_event(command)

    print_result(coffee)

def evaluate_event(event):
    if event in ["coding", "dog", "cat", "movie"]:
        return 1
    elif event.isupper():
        return 2
    else:
        return 0

def print_result(coffee):
    if coffee > 5:
        print("You need extra sleep")
    else:
        print(coffee)

count_coffees()
---------------------------------------------------------

coffee = 0

while True:
    command = input()

    if command == "END":
        break

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee += 1
    elif command.isupper():
        coffee += 2
    else:
        continue

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)

