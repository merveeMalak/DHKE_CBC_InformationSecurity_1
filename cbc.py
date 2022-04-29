#this file contains cipher blockchaining encryption and decryption algorithms

#The encryption algorithm takes as parameters the message to be encrypted,
# the initialisation vector, and the public key. Returns encrypted message
def cbc_encrypt(message, IV,key):
    message_bytes = message.encode("ascii") #encode message
    ciphertext = []
    for i in range(len(message_bytes)):
        if i == 0:  #first block is different
            first_xor = (message_bytes[i] ^(int(IV)%128))% 128 # first block xor IV 
            ciphertext.append((first_xor ^ key)% 128) # first_xor xor key
        else:
            first_xor = (message_bytes[i] ^ ciphertext[i-1])% 128 # ith block xor i-1th ciphertext
            ciphertext.append((first_xor^key)% 128) #first_xor xor key
    print(ciphertext)
    return ("".join(map(chr, ciphertext))) #returns ciphertext 


#The decryption algorithm takes as parameters the ciprtext to be decrypted,
# the initialisation vector, and the public key. Returns decrypted message
def cbc_decrypt(ciphertext, IV, key):
    ciphertext_bytes = ciphertext.encode("ascii") #ciphertext encode
    plaintext = []
    for i in range(len(ciphertext_bytes)):
        if i == 0: #first block is different
            first_xor = (ciphertext_bytes[i] ^ key) % 128 # (first block xor key) mod 128
            plaintext.append((first_xor ^ (int(IV)%128)) % 128)  # (first_xor xor IV) mod 128
        else:
            first_xor =  (ciphertext_bytes[i] ^key)% 128 #(i-th block xor key) mod 128
            plaintext.append((first_xor ^ ciphertext_bytes[i-1])% 128) #(first_xor xor i-1th block) mod 128
    return ("".join(map(chr, plaintext))) # returns message
            

