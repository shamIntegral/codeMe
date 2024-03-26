from primeGenerator import primeGenerate 

def primeCheak(num):
    prime_list = primeGenerate(num + 5)
    for primes in prime_list:
        if num == primes:
            return True
        else: pass
    return False

# Test :

#sample_num = int(input("Which number you want to cheak: "))
#if primeCheak(sample_num):
#    print("It's Prime Number")
#else :
#    print("Its Composite number")    

