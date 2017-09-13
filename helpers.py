def alphabet_position(letter):
    global alpha_list 
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_position = alpha_list.index(letter.lower()) + 1
    return alpha_position

def rotate_character(char, rot):
    rot_char = char
    if char.isalpha():
        init_index = alphabet_position(char)
        if init_index + rot > 26:
            rot_char = alpha_list[((init_index+rot) - 27)]
        else:
            rot_char = chr((ord(char)) + rot)
        if char.isupper():
            rot_char = rot_char.upper()
        
    return rot_char