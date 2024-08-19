def collect_item(items, item):
    if item not in items:
        items.append(item)


def drop_item(items, item):
    if item in items:
        items.remove(item)


def combine_items(items, old_item, new_item):
    if old_item in items:
        index = items.index(old_item)
        items.insert(index + 1, new_item)


def renew_item(items, item):
    if item in items:
        items.remove(item)
        items.append(item)


def print_items(items):
    print(', '.join(items))


def main():
    items = input().split(', ')

    while True:
        command = input().split(' - ')

        if command[0] == 'Craft!':
            break

        if command[0] == 'Collect':
            collect_item(items, command[1])

        elif command[0] == 'Drop':
            drop_item(items, command[1])

        elif command[0] == 'Combine Items':
            old_item, new_item = command[1].split(':')
            combine_items(items, old_item, new_item)

        elif command[0] == 'Renew':
            renew_item(items, command[1])

    print_items(items)


main()
