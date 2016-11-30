import math

#проверка числа на простоту
def is_prime(n):
    divisor = 2
    while n % divisor != 0:
        divisor = divisor + 1
    if divisor == n:
        is_prime = True
    else:
        is_prime = False
    return is_prime


# алгоритм Евклида, проверка на взаимную простоту; 
# НОД(a, b) = НОД(b, a % b)
# даны два натуральных числа a и b, необходимо найти такое наибольшее число d, 
# которое является делителем каждого из этих чисел
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

#рассширенный алгоритм евлида, нвхождение  такого числа d = d * e mod phi = 1
#на входе числа a и b
#возвращает 3 числа d, x, y (d - НОД)
#когда b = 0, конец
#d = a, x = 1, y = 0  
def multiplicative_inverse(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = multiplicative_inverse(b, a % b)
        return d, y, x - y * (a // b)


def generate_keypair(p, q):
    p = int(p)
    q = int(q)
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p*q
    phi = (p-1)*(q-1) #функция эйлера

    #числo e должно быть простое, меньше phi и взаимнопростое с phi \
    
    for i in range(3, phi, 2):
        if is_prime(i) and gcd(phi, i) == 1:
            e = i
            break
    x, y, d = multiplicative_inverse(phi, e)
    d = d % phi
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)



if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
