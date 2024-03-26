import math
from primeCheak import primeCheak

# for number with non-reapting digits.
def permute(num):
    str_num = str(num)
    total_digit = len(str_num)

    permutations = []

    for i in range(0, total_digit):
        for j in range(0, total_digit):
            for k in range(0, total_digit):
                for l in range(0, total_digit):
                    permuted_num = str_num[i] + str_num[j] + str_num[k] + str_num[l]
                    permutations.append(int(permuted_num))

    return permutations

number = int(input("Number: "))
Permutations_list = permute(number)

prime_in_permutations_list = []

for num in Permutations_list:
    if primeCheak(num):
        prime_in_permutations_list.append(num)
    else: pass    

print(prime_in_permutations_list)
