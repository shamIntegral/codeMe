import math

def primeGenerate(max):
    prime_list = [2]
    for num in range(3, max + 1):
        result_list = []
        for primes in prime_list:
            if primes <= (math.sqrt(num) + 1):
                if num % primes != 0:
                    result_list.append("True")
                else: 
                    result_list.append("False")
            else: 
                break    

        if result_list.count("False") == 0:
            prime_list.append(num)
        else:
            pass

    return prime_list

#lowerLimit = int(input("From what prime numbers you need: "))
upperLimit = int(input("Upto what prime numbers you need: "))
Prime_list = primeGenerate(upperLimit)
    
print(Prime_list)
print(f"Total primes upto {upperLimit} is: {len(Prime_list)}")
