first_string = input()
second_string = input()
while first_string in second_string:
    second_string = second_string.replace(first_string, '')

print(second_string)



=====================================================

class StringManipulator:
    def __init__(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string

    def remove_occurrences(self):
        while self.first_string in self.second_string:
            index = self.second_string.find(self.first_string)
            if index != -1:
                self.second_string = self.second_string[:index] + self.second_string[index + len(self.first_string):]

        return self.second_string

first_line = input()
second_string = input()

manipulator = StringManipulator(first_line, second_string)
result = manipulator.remove_occurrences()
print(result)


=================================================================


first_line = input()
second_string = input()

while True:
    index = second_string.find(first_line)
    if index == -1:
        break
    second_string = second_string[:index] + second_string[index + len(first_line):]

print(second_string)

