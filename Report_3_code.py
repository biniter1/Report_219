import numpy as np
import string

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
         if (a * x) % m == 1:
             return x
    return None  

def get_inverse_key_matrix(key_matrix):
    a, b, c = key_matrix[0]
    d, e, f = key_matrix[1]
    g, h, i = key_matrix[2]
    
    det = (a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)) % 26
    inv_det = mod_inverse(det, 26)
    if inv_det is None:
        return None

    A = (e*i - f*h) % 26
    B = (- (d*i - f*g)) % 26
    C = (d*h - e*g) % 26
    D = (- (b*i - c*h)) % 26
    E = (a*i - c*g) % 26
    F = (- (a*h - b*g)) % 26
    G = (b*f - c*e) % 26
    H = (- (a*f - c*d)) % 26
    I = (a*e - b*d) % 26

    adjugate = [
        [A, D, G],
        [B, E, H],
        [C, F, I]
    ]
    
    inv_matrix = [[(adjugate[row][col] * inv_det) % 26 for col in range(3)]
                  for row in range(3)]
    
    
    inv_matrix = [[num if num >= 0 else num + 26 for num in row] for row in inv_matrix]
    return inv_matrix

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper()
    letters = [char for char in plaintext if char in string.ascii_uppercase]
    while len(letters) % 3 != 0:
        letters.append('X')
    
    ciphertext = ""
    letter_idx = 0
    for char in plaintext:
        if char not in string.ascii_uppercase:
            ciphertext += char
        else:
            if letter_idx % 3 == 0:
                block = letters[letter_idx: letter_idx+3]
                block_vector = [ord(block[i]) - ord('A') for i in range(3)]
                encrypted_vector = [(sum(key_matrix[i][j] * block_vector[j] for j in range(3))) % 26 for i in range(3)]
                cipher_block = "".join(chr(num + ord('A')) for num in encrypted_vector)
                ciphertext += cipher_block
            letter_idx += 1
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    inv_key = get_inverse_key_matrix(key_matrix)
    if inv_key is None:
        raise ValueError("The key matrix is not invertible modulo 26.")
    
    ciphertext = ciphertext.upper()
    letters = [char for char in ciphertext if char in string.ascii_uppercase]
    while len(letters) % 3 != 0:
        letters.append('X')
    
    plaintext = ""
    letter_idx = 0
    for char in ciphertext:
        if char not in string.ascii_uppercase:
            plaintext += char
        else:
            if letter_idx % 3 == 0:
                block = letters[letter_idx: letter_idx+3]
                block_vector = [ord(block[i]) - ord('A') for i in range(3)]
                decrypted_vector = [(sum(inv_key[i][j] * block_vector[j] for j in range(3))) % 26 for i in range(3)]
                plain_block = "".join(chr(num + ord('A')) for num in decrypted_vector)
                plaintext += plain_block
            letter_idx += 1
    return plaintext

def generate_key(size, mod=26):
    while True:
        ma_tran = np.random.randint(0, mod, (size, size))
        det = int(round(np.linalg.det(ma_tran))) % mod
        if np.gcd(det, mod) == 1:
            return ma_tran

def print_key_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:3}" for num in row))

def main():
    key_to_decrypt = tao_key(3)
    print_key_matrix(key_to_decrypt)
    key_inverse = get_inverse_key_matrix(key_to_decrypt)
    
    if key_inverse is None:
        print("The generated matrix is not invertible. Generating a new one...")
        return
    
    plaintext = input("Enter your input to encrypt: ")
    ciphertext = hill_encrypt(plaintext, key_to_decrypt)
    print("\nCiphertext:", ciphertext)
    
    decrypted_text = hill_decrypt(ciphertext, key_to_decrypt)
    print("\nDecrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
