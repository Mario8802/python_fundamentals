repeat_string = lambda string, n: string * n


string = input()
counter = int(input())
result = repeat_string(string,counter)
print(result)




def repeat_string(text, num):
    return text * num


string = input()
n = int(input())

print(repeat_string(string, n))
