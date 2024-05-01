def sort_names():
    names_list = [name for name in input().split(', ')]

    return sorted(names_list, key=lambda name: (-len(name), name))

print(sort_names())


def sorted_names(some_names):
    return sorted(some_names, key=lambda x: (-len(x), x))


names = input().split(', ')
print(sorted_names(names))
