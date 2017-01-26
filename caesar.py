def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ix in range(len(alphabet)):
        if alphabet[ix] == letter.lower():
            return ix

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha() != True:
        return char
    elif char.isupper() == True:
        num = (alphabet_position(char) + rot) % 26
        return alphabet[num].upper()
    else:
        num = (alphabet_position(char) + rot) % 26
        return alphabet[num]

def encrypt(text, rot):
    if text == "":
        return text
    char = text[0]
    encrypt_text = []
    for char in text:
        encrypt_char = rotate_character(char, rot)
        encrypt_text.append(encrypt_char)
    encrypt_text = "".join(encrypt_text)
    return encrypt_text
