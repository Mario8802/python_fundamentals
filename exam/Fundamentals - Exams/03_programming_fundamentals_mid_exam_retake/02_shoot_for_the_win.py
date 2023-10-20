sequence_with_integers = list(map(int, input().split()))
command = input()
count_of_shot_targets = 0
list_with_indexes = []

while command != 'End':
    index = int(command)

    if index+1 > len(sequence_with_integers):
        command = input()
        continue

    if index not in list_with_indexes:
        list_with_indexes.append(index)
        num_on_the_index = sequence_with_integers[index]
        current_target = - 1
        count_of_shot_targets += 1
        sequence_with_integers[index] = current_target

        for i in range(len(sequence_with_integers)):
            
            if sequence_with_integers[i] <= num_on_the_index and sequence_with_integers[i] != -1:
                sequence_with_integers[i] = sequence_with_integers[i] + num_on_the_index
                
            elif sequence_with_integers[i] > num_on_the_index and sequence_with_integers != -1:
                sequence_with_integers[i] = sequence_with_integers[i] - num_on_the_index

    command = input()

string_integer_list = list(map(str, sequence_with_integers))
print(f'Shot targets: {count_of_shot_targets} -> {" ".join(string_integer_list)}')