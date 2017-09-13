from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted_text = ''
    for char in text:
        encrypted_text += rotate_character(char, rot)
    return encrypted_text
 
def main():
    from sys import argv, exit

    if argv[1].isdigit == False:
        text, rot = input("Type a message: \n"), int(argv[1])
        print(encrypt(text, rot))
    else:
        print('usage: python caesar.py n')
        exit()

if __name__ == "__main__":
    main()









