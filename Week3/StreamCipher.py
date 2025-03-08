#!/usr/bin/env python3
import os

def logistic_map_keygen(length: int, x0: float, r: float) -> bytes:
    x = x0
    key = bytearray(length)
    for i in range(length):
        if x<0.5:
            x=r*x
        else:
            x=r*(1.0-x)
        key[i] = int(x * 256) & 0xFF
        
    return bytes(key)

def chaotic_encrypt_decrypt(input_path: str, output_path: str, x0: float, r: float):

    with open(input_path, 'rb') as f_in:
        data = f_in.read()

    length = len(data)
    key = logistic_map_keygen(length, x0, r)
    
    result = bytes(d ^ k for d, k in zip(data, key))
    
    with open(output_path, 'wb') as f_out:
        f_out.write(result)

def main():
    print("=== Chaotic Map (Logistic) Stream Cipher Demo ===")
    print("This script uses a simple XOR-based scheme with a Logistic map keystream.")
    print("Disclaimer: Not secure for real-world cryptography.\n")
    
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")
        return
    
    input_file = input("Enter path to input file: ").strip()
    output_file = input("Enter path to output file: ").strip()
    
    try:
        x0 = float(input("Enter logistic map seed x0 (0 < x0 < 1): ").strip())
        r = float(input("Enter logistic map parameter r (1 < r < 2): ").strip())
    except ValueError:
        print("Invalid x0 or r. Must be float.")
        return
    
    if not (0 < x0 < 1):
        print("x0 must be between 0 and 1.")
        return
    
    chaotic_encrypt_decrypt(input_file, output_file, x0, r)
    
    print(f"\nDone. {'Encrypted' if mode=='encrypt' else 'Decrypted'} file saved to '{output_file}'.")

if __name__ == "__main__":
    main()
