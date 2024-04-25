# Write a program that receives a sequence of numbers (integers)
# separated by a single space. It should print the min and max values
# of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().


sequence_of_integers = [int(x) for x in input().split()]

print(f"The minimum number is {min(sequence_of_integers)}")
print(f"The maximum number is {max(sequence_of_integers)}")
print(f"The sum number is: {sum(sequence_of_integers)}")
