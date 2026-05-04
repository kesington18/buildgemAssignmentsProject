letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

def encrypt(txt, shft):
    res = ""
    for letter in txt:
        val = letters.index(letter) + shft
        val %= len(letters)
        res += letters[val]

    print(f"Here is the encoded result: {res}")

if direction == 'encode':
    encrypt(text, shift)
