import random
from hashlib import sha256

def gcd(a,b):
    if a==b:
        return a
    elif a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)
    
def is_prime(n, k=128):
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randrange(2, n)
        x = pow(a, n - 1, n)
        if x != 1:
            return False
    return True

def generate_large_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

p = generate_large_prime(100)
q = generate_large_prime(100)

n=p*q
print(n)

k=(p-1)*(q-1)
print(k)

def generate_e(x):
    while True:
        e = random.randrange(2, x)
        if gcd(e, x) == 1:
            return e

e = generate_e(k)
print(e)

if e<k:
    print("true")

def modinv(e, k):
    g, x, y = egcd(e, k)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % k

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

d=modinv(e,k)

def encrypt_rsa(message: int, n: int, e: int):
 
    encrypted_text = pow(message, e, n)
    return encrypted_text

def decrypt_rsa(encrypted_text: int, n: int, d: int):

    decrypted_text = pow(encrypted_text, d, n)
    return decrypted_text


message = 289
print("Message is",message)
encrypted_text = encrypt_rsa(message, n, e)
print(encrypted_text) 
decrypted_text = decrypt_rsa(encrypted_text, n, d)
print("After decryption:",decrypted_text)




def sign_message(message, n, e, d):
   
    h = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')

    signature = pow(h, d, n)
    return signature

def verify_signature(message, signature, n, e):
  
    h = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')
  
    return pow(signature, e, n) == h


message = "Hello, World!"
signature = sign_message(message, n, e, d)


is_valid = verify_signature(message, signature, n, e)
print(f"Is the signature valid? {is_valid}")


is_valid = verify_signature("Goodbye, World!", signature, n, e)
print(f"Is the signature valid? {is_valid}")

