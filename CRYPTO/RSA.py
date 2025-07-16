# The following program implements the RSA algorithm for encryption and signatures.
# Greatest Common Divisor Function
def gcd(a, b):
    while b != 0:
        r = b
        b = a % b
        a = r
    return a


# Least Common Multiple
def lcm(a, b):
    num = a * b
    den = gcd(a, b)
    return num // den


# Validating Public Key
def validate_public_key(key, carmichael):
    if key < 1:
        print("Key too low! Try Again!")
    if key > carmichael:
        print("Key too high! Try Again!")
    if gcd(key, carmichael) != 1:
        print("Key is not co-prime to Carmichael! Try Again!")
        quit()


# Find Private Key
def find_private_key(key, modulus):
    r = [modulus, key]
    q = [0, 0]
    a = [0, 1]
    index = 2
    while r[len(r) - 1] != 0:
        quotient = r[index - 2] // r[index - 1]
        q.append(quotient)
        remainder = r[index - 2] - q[index] * r[index - 1]
        r.append(remainder)
        aux = a[index - 2] - q[index] * a[index - 1]
        a.append(aux)
        index += 1
    inverse = a[len(a) - 2]
    if inverse < 0:
        inverse += modulus
    return inverse


# RSA Encrypt
def RSA_encrypt(message, key, modulus):
    cipherlist = []
    for c in message:
        number = ord(c)
        cipher = (number ** key) % modulus
        cipherlist.append(cipher)
    return cipherlist


# RSA Decrypt
def RSA_decrypt(cipher, key, modulus):
    message = ""
    for n in range(len(cipher)):
        number = (cipher[n] ** key) % modulus
        message += chr(number)
    return message


# Hash Function
def new_hash(message):
    digest = 0
    for c in message:
        digest += ord(c)
        digest = digest % 256
    return digest


# Write Signature
def write_signature(message, key, modulus):
    hashed_text = new_hash(message)
    signature = (hashed_text ** key) % modulus
    return signature


# Check Signature
def check_signature(message, signature, key, modulus):
    hashed_text = new_hash(message)
    hash_check = signature ** key % modulus
    if hashed_text == hash_check:
        print("Transaction is valid! Please wait while a new block is generated!" + "\n")
        return True
    else:
        print("Transaction is invalid" + "\n")
        return False


# Prime Numbers
primeP = 61
primeQ = 53
# Carmichael Function
carmichael = lcm(primeP - 1, primeQ - 1)
# Find Modulus
modulus = primeP * primeQ

# Alice Public Key
alice_public_key = 17
# Validate the Key
validate_public_key(alice_public_key, carmichael)
# Find Private Key
alice_private_key = find_private_key(alice_public_key, carmichael)

"""
# Send a Message
alice_plaintext = "Hello B"
alice_signature = write_signature(alice_plaintext, alice_private_key, modulus)
alice_message = "Hello B."
check_signature(alice_message, alice_signature, alice_public_key, modulus)
"""