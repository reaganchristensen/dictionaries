#Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:
#codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .} 
#Using this example, the letter A would be assigned the symbol %, the letter a would be assigned the number 9,
#the letter B would be assigned the symbol @, and so forth. 
#The program should open this file -  info_security.txt Download info_security.txt, read its contents, 
#then use the dictionary to write an encrypted version of the file’s contents to a second file (name it 'encrypted.txt'). 
#Each character in the second file should contain the code for the corresponding character in the first file.

# Dictionary to assign codes to letters
codes = {
    'A': '%', 'a': '9',
    'B': '@', 'b': '#',
    'C' : '!', 'c': '1',
    'D': '$', 'd' : '2',
    'E': '4', 'e': '5',
    'F': '^', 'f': '6',
    'G': '&', 'g': '7',
    'H': '*', 'h': '8',
    'I': '10', 'i': '~',
    'J': '%', 'j': '9',
    'K': '@', 'k': '#',
    'L' : '!', 'l': '1',
    'M': '$', 'm' : '2',
    'N': '4', 'n': '5',
    'O': '^', 'o': '6',
    'P': '&', 'p': '7',
    'Q': '*', 'q': '8',
    'R': '10', 'r': '~',
    'S': '%', 's': '9',
    'T': '@', 't': '#',
    'U' : '!', 'u': '1',
    'V': '$', 'v' : '2',
    'W': '4', 'w': '5',
    'X': '^', 'x': '6',
    'Y': '&', 'y': '7',
    'Z': '*', 'z': '8',
}

txtfile = open('info_security.txt', 'r')

original_text = txtfile.read()

def encrypt_text(text, codes):
    encrypted_text = ""
    for char in text:
        if char in codes:
            encrypted_text += codes[char]
        else:
            encrypted_text += char
    return encrypted_text


encrypted_text = encrypt_text(original_text, codes)

encrypted_file = open('encrypted.txt', 'w')

encrypted_file.write(encrypted_text)