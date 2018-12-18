import string
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    new_text = ''
    count = 0
    k = 0
    for i in text:
        if i.isalpha():
            k = alphabet_position(key[count])
            new_text = new_text + rotate_character(i, k)
            count = ((count + 1) % len(key))
        else:
            new_text = new_text + i
       
    return new_text

def main():
    
    message = str(input("Type a message: "))
    print(message)
    key = str(input("Encryption key: "))
    print(key)
    print(encrypt(message, key))

if __name__ == "__main__":
    main()