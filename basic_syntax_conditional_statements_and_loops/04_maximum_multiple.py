# divisor = int(input())
# boundary = int(input())
#
# for num in range(boundary,divisor - 1, -1):
#     if num % divisor == 0:
#         break
# print(num)
#
#


divisor = int(input())
boundary = int(input())

output = int(boundary / divisor) * divisor
print(output)
