# -*- coding: utf-8 -*-
#Ref: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf
# Mode: https://csrc.nist.gov/pubs/sp/800/38/a/sup/final
import sys, os
sys.path.append(os.getcwd()) # get curent working dir and export to python paths
from mypackages import key_expansion,modes

# Convert text <--> bin
def message_to_bin(message):
    """Convert a string message to its binary representation using UTF-8 encoding."""
    binary_message = ''.join(format(byte, '08b') for byte in message.encode('utf-8'))
    return binary_message
def read_file(input_file):
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found!")
        sys.exit(1)
    with open(input_file, 'rb') as f:
        return f.read()
def write_file(output_file,data):
    with open(output_file, 'wb') as f:
        return f.write(data)
def aes_mode_test(mode,input_file,output_file):
    # key128 for testing, we may revide this funtion to def aes_mode_test(mode, key)
    key128 = "12345678abcdefgh"
    key_bytes_128 = key128.encode('utf-8')
    aes_mode = modes.modes(key_bytes_128)

    data=read_file(input_file)
    if isinstance(data, str):  # Nếu data là string, cần chuyển đổi sang bytes
        data = data.encode()

    if mode == "ECB":
        cipher = aes_mode.ecb_encrypt(data)
        decrypt_function = aes_mode.ecb_decrypt
    elif mode == "CBC":
        cipher = aes_mode.cbc_encrypt(data)
        decrypt_function = aes_mode.cbc_decrypt
    elif mode == "CFB":
        cipher = aes_mode.cfb_encrypt(data)
        decrypt_function = aes_mode.cfb_decrypt
    elif mode == "OFB":
        cipher = aes_mode.ofb_encrypt(data)
        decrypt_function = aes_mode.ofb_decrypt
    elif mode == "CTR":
        cipher = aes_mode.ctr_encrypt(data)
        decrypt_function = aes_mode.ctr_decrypt
    else:
        print("Invalid mode!")
        return

    print(f"Ciphertext ({mode} mode) in bytes: ", cipher, "\n")
    print(f"Ciphertext ({mode} mode) in hex: ", cipher.hex(), "\n")
    print(f"Length of Ciphertext (bytes): ", len(cipher), "\n")
    print(f"File {input_file} have encoded and saved in {output_file}")
    write_file(output_file,cipher)

    cipher_file=input("Enter file name to decrypt:")
    plainfile=input("Enter file name to save decrypted file:")
    data=read_file(cipher_file)
    recovered_text = decrypt_function(data)


    print(f"Recovered text ({mode} mode): ", recovered_text, "\n")
    print(f"File {input_file} have decoded and saved in {plainfile}")
    write_file(plainfile, recovered_text.encode('utf-8'))



##Main part
if __name__ == "__main__":
    print("Select AES mode:")
    print("1. ECB")
    print("2. CBC")
    print("3. CFB")
    print("4. OFB")
    print("5. CTR")
    choice = input("Enter choice (1/2/3/4/5): ")

    mode_map = {
        "1": "ECB",
        "2": "CBC",
        "3": "CFB",
        "4": "OFB",
        "5": "CTR"
    }
    input_file=input("Enter the name of the input file:")
    output_file=input("Enter the name of the output file:")
    selected_mode = mode_map.get(choice)
    if selected_mode:
        aes_mode_test(selected_mode,input_file,output_file)
    else:
        print("Invalid choice!")

#Test key 128
key128="12345678abcdefgh"
key_bytes_128 = key128.encode('utf-8')
AES128_keys = key_expansion.key_expansion(key_bytes_128).key_expansion_128()
print("\n Extension key for 10 rounds:", AES128_keys, "\n Number of words (4 bytes each):",len(AES128_keys))

#Test key 192
key192="12345678abcdefghvbnmfgds"
key_bytes_192 = key192.encode('utf-8')
AES192_keys = key_expansion.key_expansion(key_bytes_192).key_expansion_192()
#print(AES192_keys,"number of words:",len(AES192_keys))

#Test key 256

key256="12345678abcdefghvbnmfgds12345678"
key_bytes_256=key256.encode('utf-8')
AES256_keys = key_expansion.key_expansion(key_bytes_256).key_expansion_256()
#print(AES256_keys,"number of words:",len(AES256_keys))
