import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    new_text = ''
    for i in text:
        new_text = new_text + rotate_character(i, rot)
    return new_text


def main():
    
    message = str(input("Type a message: "))
    print(message)
    rotation = int(input("Rotate by: "))
    print(rotation)
    print(encrypt(message, rotation))

if __name__ == "__main__":
    main()