#This file contains the mathematical algorithms that will be required 
#in key exchange, encryption and decryption stages.

import random

#If the result returns true, the number may be prime,
# but if it returns false, the number is composite.
def primality_test_base(p):
    if (p==2):  #2 is prime
        return True
    a = random.randint(2, p-1) #a is random number 
    k = p-1 
    while k > 0:
        result = modular_exponentiation(a, k, p) #returns (a**k)%p
        if (result != 1) & (k < p-1) & (result != p-1): 
            return False
        elif result == p-1: #result == -1 
            return  True
        elif (result == 1) & (k % 2 != 0):
            return  True
        else:
            k = int(k/2)

#Even if the number is prime in the primality test,
#it can be strong liar, for this, 10 times are tested.
def primality_test(p):
    for i in range(0,10):
        if not primality_test_base(p):
            return False
    return True

#returns result base**power % mod
def modular_exponentiation(base, power, mod):
    if power == 0:
        return 1
    
    result = 0
    result = modular_exponentiation(base, power//2, mod)
    if power % 2 == 0: # power is even 
        return (result * result) % mod
    else: #power is odd
        return (result * result * base) % mod

#returns prime factors of number
def prime_factor(number):
    prime_factor_list = []
    while (number % 2 == 0): #number is even
        number /= 2
        prime_factor_list.append(2)
    for i in range(3, int(number**(0.5)), 2): #continues until the square root of the number 
        while (number % i == 0): #i is the multiplier of the number
            prime_factor_list.append(i)
            number /= i
    if number > 2:
        prime_factor_list.append(number)
    return set(prime_factor_list)


#cheks g is a generator or not 
def generator_test(g,p): 
    prime_factor_list = prime_factor(p-1) #returns prime factors  
    for i in prime_factor_list:
        if (modular_exponentiation(g, (p-1)/i, p) == 1): 
            return False
    return True
