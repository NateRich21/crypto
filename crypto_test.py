import caesar

def encrypt(text, key_word):
    encrypted_text = ''
    for char in text:
        key_word_index = 0
        while key_word_index + 1 < len(key_word):
            if char.isalpha():
                rot_char = caesar.rotate_char(char, (caesar.alphabet_position(key_word[key_word_index])))
                encrypted_text += rot_char
                key_word_index += 1
            else:
                rot_char = 
                encrypted_text += rot_char
    return encrypted_text

def main():

    text = input("Please enter a sentence \n> ")
    key_word = input("Select a keyword \n> ")

    print(encrypt(text, key_word))

if __name__ == "__main__":
    main()


# use the keyword index

