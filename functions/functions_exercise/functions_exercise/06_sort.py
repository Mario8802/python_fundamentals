# Write a program that receives a sequence of numbers
# (integers) separated by a single space. It should
# print a sorted list of numbers in ascending order. Use sorted().


sequence_of_integers = [int(x) for x in input().split()]
sorted_list = sorted(sequence_of_integers)
print(sorted_list)
