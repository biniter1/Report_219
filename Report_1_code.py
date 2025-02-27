import string

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"No modular inverse for a = {a}. Please choose a value of 'a' that is coprime with 26.")
    alphabets = string.ascii_uppercase
    result = []
    for char in text:
        if char.isupper():
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            result.append(alphabets[x])
        elif char.islower():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y - b)) % 26
            result.append(alphabets[x].lower())
        else:
            result.append(char)
    return ''.join(result)

def main():
        encrypted_text = input("\nEnter the text to decrypt: ")
        for a in range(1,26,2):
            if mod_inverse(a, 26) is not None:
                for b in range(0,25):
                    decrypted_text = affine_decrypt(encrypted_text, a, b) 
                    print(f"a = {a:2}, b = {b:2} -> {decrypted_text}")
if __name__ == "__main__":
    main()