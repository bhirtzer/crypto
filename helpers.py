import string

def alphabet_position(letter):

    alphabet = string.ascii_lowercase
    letter = letter.lower()
    position = 0
    position = alphabet.index(letter)

    return position

def rotate_character(char, rot):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    while char.isalpha():
        if char.isupper():
            index = upper.find(char)
            new_char = (index + rot) % 26
            new_char = upper[new_char]
            
            return new_char

        else:
            index = lower.find(char)
            new_char = (index + rot) % 26
            new_char = lower[new_char]
            
            return new_char
    
    return char