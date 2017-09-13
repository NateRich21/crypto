from helpers import alphabet_position, rotate_character

def encrypt(text, key_word):
    encrypted_text = ''
    text_index = 0
    for position in text:
        keyword_index = 0
        while (keyword_index) < len(key_word) and text_index < len(text):
            if text[text_index].isalpha():
                rot_char = rotate_character(text[text_index],(alphabet_position(key_word[keyword_index])-1))
                keyword_index += 1
                text_index += 1
                encrypted_text += rot_char
            else:
                rot_char = text[text_index]
                text_index += 1
                encrypted_text += rot_char
    return encrypted_text
            

def main():
    from sys import argv, exit
    
    if argv[1].isalpha():
        text = input("Type a message: \n")
        key_word = argv[1]
        print(encrypt(text, key_word))
    else:
        print("""usage: python vigenere.py keyword 
Arguments:
-keyword : The string to be used as a "key" to encrypt your message. Should only co
ntain alphabetic characters-- no numbers or special characters.""")
        exit()

if __name__ == "__main__":
    main()
