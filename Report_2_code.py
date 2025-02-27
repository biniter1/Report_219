from collections import Counter
import string

english_frequencies = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

cipher_text = ("Yfhac bzc xcrcqyc vp bzc pfxyb hvicr, Zqxxs Evbbcx qhw bzc Ezfrvyvezcx'y Ybvhc, vh 26 Gjhc 1997, bzc nvvoy zqic pvjhw fkkchyc evejrqxfbs qhw avkkcxafqr yjaacyy uvxrwufwc. Bzcs zqic qbbxqabcw q ufwc qwjrb qjwfchac qy ucrr qy svjhdcx xcqwcxy qhw qxc ufwcrs avhyfwcxcw avxhcxybvhcy vp kvwcxh rfbcxqbjxc,[3][4] bzvjdz bzc nvvoy zqic xcacficw kfmcw xcifcuy pxvk axfbfay qhw rfbcxqxs yazvrqxy. Qy vp Pcnxjqxs 2023, bzc nvvoy zqic yvrw kvxc bzqh 600 kfrrfvh avefcy uvxrwufwc, kqofhd bzck bzc ncyb-ycrrfhd nvvo ycxfcy fh zfybvxs, qiqfrqnrc fh wvtchy vp rqhdjqdcy. Bzc rqyb pvjx nvvoy qrr ycb xcavxwy qy bzc pqybcyb-ycrrfhd nvvoy fh zfybvxs, ufbz bzc pfhqr fhybqrkchb ycrrfhd xvjdzrs 2.7 kfrrfvh avefcy fh bzc Jhfbcw Ofhdwvk qhw 8.3 kfrrfvh avefcy fh bzc Jhfbcw Ybqbcy ufbzfh buchbs-pvjx zvjxy vp fby xcrcqyc. Fb zvrwy bzc Djfhhcyy Uvxrw Xcavxw pvx Ncyb-ycrrfhd nvvo ycxfcy pvx azfrwxch")


cipher_counts = Counter(''.join(filter(str.isalpha, cipher_text.upper())))
sorted_cipher = ''.join([item[0] for item in cipher_counts.most_common()])


mapping = {}
for i, letter in enumerate(sorted_cipher):
    mapping[letter] = english_frequencies[i]

for letter in string.ascii_uppercase:
    if letter not in mapping:
        mapping[letter] = letter

mapping["V"]="O"
mapping["H"]="N"
mapping["B"]="T"
mapping["Z"]="H"
mapping["Q"]="A"
mapping["W"]="D"
mapping["X"]="R"
mapping["F"]="I"
mapping["R"]="L"
mapping["Y"]="S"
mapping["E"]="P"
mapping["K"]="M"
mapping["P"]="F"
mapping["U"]="W"
mapping["O"]="K"
mapping["N"]="B"
mapping["T"]="Z"

def print_key_mapping_table(mapping):

    plain_letters = list(string.ascii_uppercase)
    row1 = " ".join(f"{letter:2}" for letter in plain_letters)
    row2 = " " + "--" + "+--"*(len(plain_letters)-1) + " "
    row3 = " ".join(f"{mapping[letter]:2}" for letter in plain_letters)
    
    print(row1)
    print(row2)
    print(row3)

print_key_mapping_table(mapping)

decrypted_text = []
for char in cipher_text:
    if char.isalpha():
        if char.isupper():
            decrypted_text.append(mapping.get(char, char))
        else:
            decrypted_text.append(mapping.get(char.upper(), char.upper()).lower())
    else:
        decrypted_text.append(char)
decrypted_text = ''.join(decrypted_text)

print("\nDecrypted Text:")
print(decrypted_text)
