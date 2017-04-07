import sys
import random

#check for co prime values of phi(n) and e
def checkgcd(c, d):
    while d != 0:
        c, d = d, c % d
    return c
    
#generate the private key using Extended Euclid's Algorithm  
def inversefunc(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    tphi = phi
    
    while e > 0:
        temp1 = tphi/e
        temp2 = tphi - temp1 * e
        tphi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if tphi == 1:
        return d + phi

# make sure the e and n values are prime
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

#public and private key generator function. 
def keypairgenerator(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q

    #Phi is the totient of n. choose e value such that phi(n) and e are co prime
    phi = (p-1) * (q-1)
    print "phi", phi
    e = random.randrange(1, phi)
    #print "e value: ", e
    g = checkgcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = checkgcd(e, phi)

    d = inversefunc(e, phi)
    
    #Return public and private keypair
    return ((e, n), (d, n))

#encryption using ord by unpacking the private key and convert letters in plain text into numbers. return byte array 
def encrypt(privkey, plaintext):
    key, n = privkey
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher
    
#decryption of cipher text based on the public key using (a*b)mod m 
def decrypt(pubkey, ciphertext):
    #Unpack the key into its components
    key, n = pubkey
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    

if __name__ == '__main__':

    print "---------------------------------------------------------------\n"
    print "SIMPLE RSA ALGORITHM IMPLEMENTATION\n"
    print "---------------------------------------------------------------\n"
    e = int(raw_input("Please enter a prime interger : e : "))
    n = int(raw_input("Enter another prime number : n : "))
    print "Generating your public/private keypairs now . . ."
    print "\n"

    public, private = keypairgenerator(e, n)
    print "Your public key is ", public ," and your private key is ", private
    print "\n"
    plainmessage = raw_input("Enter a message to encrypt with your private key: ")
    enctext = encrypt(private, plainmessage)
    print "Your encrypted message is: "
    print ''.join(map(lambda x: str(x), enctext))
    print "\n"

    print "Do you want to decrypt? please enter yes or no: "
    selection = raw_input ("yes/no ")
    if selection == 'yes' :
        print "Decrypting message with public key ", public ," . . ."
        print "Your message is:"
        print decrypt(public, enctext)
    else :
        exit
