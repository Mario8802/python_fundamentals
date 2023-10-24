# Program to check if a number is prime or not

num = int(input())

# define a flag variable
flag = False

if num == 1:
    print("False")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print("False")
    else:
        print("True")