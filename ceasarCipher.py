letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

def encrypt(text):
    res = ""
    for letter in text:
        if c in letters:
