#In this file, necessary inputs are taken and key exchange, encryption and decryption functions are called.

from test_algorithm import  primality_test, generator_test
from key_exchange import public_key_exchange
from cbc import cbc_encrypt, cbc_decrypt


#key is exchanged
def process_key_exchange():
    p = int(input("Please enter a prime(p):")) #input prime number
    if not primality_test(p): #checks if p is prime
        print("The p value you entered is not a prime number!")
        return False
    g = int(input("Please enter a generator(g): ")) #input generator number
    if not generator_test(g,p): #checks if g is generator
        print("The g value you entered is not a generator!")
        return False
    a = int(input("Please enter a private key 1 (a): ")) #input private key 1
    b = int(input("Please enter a private key 2 (b): ")) #input private key 2
    key = public_key_exchange(a,b,p,g) #returns public key 
    if not key:
        print("Failed to create shared secret key!")
        return False
    return key

#encrytion and decryption are done 
def process_encryption_decryption(key):
    message = input("Please enter a message: ") #input message
    IV = input("Please enter a initialisation vector (IV) (must be number): ") #input IV valıe
    ciphertext = cbc_encrypt(message, IV, key) #returns encrypted message
    print("Ciphertext:" , ciphertext)
    plaintext = cbc_decrypt(ciphertext, IV, key) #returns decrypted message 
    print("Message: ", plaintext)


def main():
    key = process_key_exchange()
    if key:
        process_encryption_decryption(key)

        
main()