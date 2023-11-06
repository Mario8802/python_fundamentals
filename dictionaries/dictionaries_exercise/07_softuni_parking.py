n = int(input())
employees = {}
for command in range(n):
    commands = input().split()
    username = commands[1]
    if 'register' in commands:
        license_plate = commands[2]
        if username not in employees:
            employees[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif 'unregister' in commands:
        if username in employees:
            employees.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
for registered in employees.items():
    print(f"{registered[0]} => {registered[1]}")