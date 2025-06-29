import os
import base58
import base64


# Header of content
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"\n{DARK_GREEN} ____                   ______              _ _\n"       
          f"|  _ \                 |  ____|            (_) |\n"      
          f"| |_) | __ _ ___  ___  | |__ __ _ _ __ ___  _| |_   _\n" 
          f"|  _ < / _` / __|/ _ \ |  __/ _` | '_ ` _ \| | | | | |\n"
          f"| |_) | (_| \__ \  __/ | | | (_| | | | | | | | | |_| |\n"
          f"|____/ \__,_|___/\___| |_|  \__,_|_| |_| |_|_|_|\__, |\n"
          f"                   ______                        __/ |\n"
          f"                  |______|                      |___/\n "
          f"\n{RED}Created by: Github ~ DevilTanuki99\n"
         )
    
def options():
    print(f"+-----------------+\n"
          f"| 1. Base2        |\n"
          f"| 2. Base8        |\n"
          f"| 3. Base10       |\n"
          f"| 4. Base16       |\n"
          f"| 5. Base32       |\n"
          f"| 6. Base36       |\n"
          f"| 7. Base58       |\n"
          f"| 8. Base62       |\n"
          f"| 9. Base64       |\n"
          f"| 10. Base85      |\n"
          f"| 11. Exit        |\n"
          f"+-----------------+\n"
          )

def encode_decodeBanner():
    print(f"+-----------+\n"
          f"| 1. Encode |\n"
          f"| 2. Decode |\n"
          f"+-----------+"
          )
    

# Base2 tools
def encode_base2(text):
    return ' '.join(format(ord(c), '08b')
                   for c in text)
def decode_base2(binary_str):
    try:
        chars = binary_str.split()
        return ' '.join(chr(int(b, 2))
                       for b in chars)
    except ValueError:
        return "❌Invalid Input!❌"

# Base8 tools
def encode_base8(text):
    return ' '.join(format(ord(c), '03o')
                   for c in text)
def decode_base8(octal_str):
    try:
        chars = octal_str.split()
        return ''.join(chr(int(o, 8))
                       for o in chars)
    except ValueError:
        return "❌Invalid Input!❌"
    
# Base10 tools
def encode_base10(text):
    return ' '.join(str(ord(c))
                   for c in text)
def decode_base10(number_str):
    try:
        codes = number_str.split()
        return ''.join(chr(int(n))
                       for n in codes)
    except ValueError:
        return "❌Invalid Input!❌"

# Base16 tools
def encode_base16(text):
    return text.encode('utf-8').hex()
def decode_base16(hex_str):
    try:
        return bytes.fromhex(hex_str).decode('utf-8')
    except ValueError:
        return "❌Invalid Input!❌"

# Base32 tools
def encode_base32(text):
    encoded = base64.b32encode(text.encode('utf-8'))
    return encoded.decode('utf-8')
def decode_base32(base32_str):
    try:
        decoded = base64.b32decode(base32_str)
        return decoded.decode('utf-8')
    except ValueError:
        return "❌Invalid Input!❌"

# Base36 tools
def intToBase36(n):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        n, r = divmod(n, 36)
        result = chars[r] + result
    return result
def encode_base36(text):
    return ' '.join(intToBase36(ord(c))
                   for c in text)
def decode_base36(base36_str):
    try:
        parts = base36_str.split()
        return ''.join(chr(int(part, 36))
                       for part in parts)
    except ValueError:
        return "❌Invalid Input!❌"
    
# Base58 tools
def encode_base58(text):
    encoded_bytes = base58.b58encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')
def decode_base58(b58_text):
    try:
        decoded_bytes = base58.b58decode(b58_text)
        return decoded_bytes.decode('utf-8')
    except ValueError:
        return "❌Invalid Input!❌"

# Base62 tools
BASE62_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def intToBase62(n):
    if n == 0:
        return "00"
    result = ""
    while n > 0:
        n, r = divmod(n, 62)
        result = BASE62_CHARS[r] + result
    return result.zfill(2)
def base62ToInt(s):
    total = 0
    for char in s:
        total = total * 62 + BASE62_CHARS.index(char)
    return total
def encode_base62(text):
    return ' '.join(intToBase62(ord(c)) 
                    for c in text)
def decode_base62(base62_str):
    try:
        parts = base62_str.strip().split()
        return ''.join(chr(base62ToInt(part)) for part in parts)
    except Exception as e:
        return f"❌ Invalid Input: {e}"

# Base64 tools
def encode_base64(text):
    encode = base64.b64encode(text.encode('utf-8'))
    return encode.decode('utf-8')
def decode_base64(encoded_str):
    try:
        decode = base64.b64decode(encoded_str)
        return decode.decode('utf-8')
    except ValueError:
        return "❌Invalid Input!❌"

# Base85 tools
def encode_base85(text):
    encode = base64.b85encode(text.encode('utf-8'))
    return encode.decode('utf-8')
def decode_base85(encoded_str):
    try:
        decode = base64.b85decode(encoded_str)
        return decode.decode('utf-8')
    except ValueError as e:
        return f"❌ Invalid Input: {e}"


# Option 1 - 10
def option1():
    choice_2 = input("Choose an option (1/2): ")
    if choice_2 == "1":
        plaintext_2 = input(f"{RED}Input plainText: ")
        result1_2 = encode_base2(plaintext_2)
        print(f"Encoded Base2: {result1_2}")
    elif choice_2 == "2":
        binaryText_2 = input(f"{RED}Input Base2 (space-separated): ")
        try: 
            result2_2 = decode_base2(binaryText_2)
            print(f"Decoded plainText: {result2_2}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")
    
def option2():
    choice_8 = input("Choose an option (1/2): ")
    if choice_8 == "1":
        plaintext_8 = input(f"{RED}Input plainText: ")
        result_8 = encode_base8(plaintext_8)
        print(f"Encoded Base8: {result_8}")
    elif choice_8 == "2":
        base_8 = input(f"{RED}Input Base8 (space-separated): ")
        try: 
            result2_8 = decode_base8(base_8)
            print(f"Decoded plainText: {result2_8}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

def option3():
    choice_10 = input("Choose an option (1/2): ")
    if choice_10 == "1":
        plaintext_10 = input(f"{RED}Input plainText: ")
        result1_10 = encode_base10(plaintext_10)
        print(f"Encoded Base10: {result1_10}")
    elif choice_10 == "2":
        base_10 = input(f"{RED}Input Base10 (space-separated): ")
        try: 
            result2_10 = decode_base10(base_10)
            print(f"Decoded plainText: {result2_10}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

def option4():
    choice_16 = input("Choose an option (1/2): ")
    if choice_16 == "1":
        plaintext_16 = input(f"{RED}Input plainText: ")
        result1_16 = encode_base16(plaintext_16)
        print(f"Encoded Base16: {result1_16}")
    elif choice_16 == "2":
        base_16 = input(f"{RED}Input Base16: ")
        try: 
            result2_16 = decode_base16(base_16)
            print(f"Decoded plainText: {result2_16}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

def option5():
    choice_32 = input("Choose an option (1/2): ")
    if choice_32 == "1":
        plaintext_32 = input(f"{RED}Input plainText: ")
        result1_32 = encode_base32(plaintext_32)
        print(f"Encoded Base32: {result1_32}")
    elif choice_32 == "2":
        binaryText_32 = input(f"{RED}Input Base32: ")
        try: 
            result2_32 = decode_base32(binaryText_32)
            print(f"Decoded plainText: {result2_32}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

def option6():
    choice_36 = input("Choose an option (1/2): ")
    if choice_36 == "1":
        plaintext_36 = input(f"{RED}Input plainText: ")
        result1_36 = encode_base36(plaintext_36)
        print(f"Encoded Base32: {result1_36}")
    elif choice_36 == "2":
        binaryText_36 = input(f"{RED}Input Base36: ")
        try: 
            result2_36 = decode_base36(binaryText_36)
            print(f"Decoded plainText: {result2_36}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

def option7():
    choice_58 = input("Choose an option (1/2): ")
    if choice_58 == "1":
        plaintext_58 = input(f"{RED}Input plainText: ")
        result1_58 = encode_base58(plaintext_58)
        print(f"Encoded Base58: {result1_58}")
    elif choice_58 == "2":
        binaryText_58 = input(f"{RED}Input Base58: ")
        try: 
            result2_58 = decode_base58(binaryText_58)
            print(f"Decoded plainText: {result2_58}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

def option8():
    choice_62 = input("Choose an option (1/2): ")
    if choice_62 == "1":
        plaintext_62 = input(f"{RED}Input plainText: ")
        result1_62 = encode_base62(plaintext_62)
        print(f"Encoded Base62: {result1_62}")
    elif choice_62 == "2":
        binaryText_62 = input(f"{RED}Input Base62: ")
        try: 
            result2_62 = decode_base62(binaryText_62)
            print(f"Decoded plainText: {result2_62}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

def option9():
    choice_64 = input("Choose an option (1/2): ")
    if choice_64 == "1":
        plaintext_64 = input(f"{RED}Input plainText: ")
        result1_64 = encode_base64(plaintext_64)
        print(f"Encoded Base64: {result1_64}")
    elif choice_64 == "2":
        binaryText_64 = input(f"{RED}Input Base62: ")
        try: 
            result2_64 = decode_base64(binaryText_64)
            print(f"Decoded plainText: {result2_64}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

def option10():
    choice_85 = input("Choose an option (1/2): ")
    if choice_85 == "1":
        plaintext_85 = input(f"{RED}Input plainText: ")
        result1_85 = encode_base85(plaintext_85)
        print(f"Encoded Base85: {result1_85}")
    elif choice_85 == "2":
        binaryText_85 = input(f"{RED}Input Base85: ")
        try: 
            result2_85 = decode_base85(binaryText_85)
            print(f"Decoded plainText: {result2_85}")
        except ValueError:
            print("Invalid Input!")
    print(f"{RESET}")

# Colors for terminal
GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


# Main menu
def menu():
    clear()
    banner()
    while True:
        print(f"{GREEN}")
        options()
        option = input("Choose an option: ")

        if option == "1":
            encode_decodeBanner()
            option1()
        elif option == "2":
            encode_decodeBanner()
            option2()
        elif option == "3":
            encode_decodeBanner()
            option3()
        elif option == "4":
            encode_decodeBanner()
            option4()
        elif option == "5":
            encode_decodeBanner()
            option5()
        elif option == "6":
            encode_decodeBanner()
            option6()
        elif option == "7":
            encode_decodeBanner()
            option7()
        elif option == "8":
            encode_decodeBanner()
            option8()
        elif option == "9":
            encode_decodeBanner()
            option9()
        elif option == "10":
            encode_decodeBanner()
            option10()
        elif option == "11":
            tanya = input(f"{CYAN}Quit? (y/n): ")
            if tanya.lower() == "y":
                print(f"{RESET}")
                break
            else:
                continue


def main():
    menu()


if __name__ == "__main__":
    main()