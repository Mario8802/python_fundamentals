phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone_number = entry.split("-")
    phonebook[name] = phone_number
searches = int(entry)
for search in range(searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")



# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name
# and print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."


=================================================================================




phone_book = dict()

while True:
    data = input()
    if "-" not in data:
        break
    name, phone_number = data.split("-")

    phone_book[name] = phone_number

range_of_searching = int(data)

for _ in range(range_of_searching):
    contact = input()
    
    if contact in phone_book.keys():
        print(f"{contact} -> {phone_book[contact]}")

    else:
        print(f"Contact {contact} does not exist.")
