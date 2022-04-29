#this file contains diffie hellman key exchange algorithm

from test_algorithm import modular_exponentiation


#a is the first private key, b is the second private key,
# p is the prime number and g is the generator
#return public key
def public_key_exchange(a,b,p,g):
    private_key1_result = modular_exponentiation(g,a,p) # return g**a %p
    private_key2_result = modular_exponentiation(g, b, p) #return g**b %p 
    shared_secret1 = modular_exponentiation(private_key2_result,a, p) #return ((g**b)%p)**a %p
    shared_secret2 =  modular_exponentiation(private_key1_result,b, p) #return ((g**a)%p)**b %p
    if ( shared_secret1 == shared_secret2): #if results are same
        return shared_secret1
    return False