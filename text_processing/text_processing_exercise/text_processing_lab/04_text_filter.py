banned_list = input().split(', ')
data = input()

for string in banned_list:
    while string in data:
        data = data.replace(string, '*' * len(string))

print(data)