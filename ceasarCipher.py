letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

def encrypt(txt, shft):
    res = ""
    for letter in txt:
        val = letters.index(letter) + shft
        val %= len(letters)
        res += letters[val]

    print(f"Here is the encoded result: {res}")

def decrypt(txt, shft):
    res = ""
    for letter in txt:
        val = letters.index(letter) - shft
        val %= len(letters)
        res += letters[val]
    print(f"Here is the decoded result: {res}")

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("Please enter either 'encode' or 'decode'")
'''

''' Angela Yu Solution '''
def ceaser(txt, shft, encode_or_decode):
    res = ""

    if encode_or_decode == 'decode':
        shft *= -1

    for letter in txt:
        if letter not in letters:
            res += letter
        else:
            shiftedPosition = letters.index(letter) + shft
            shiftedPosition %= len(letters)
            res += letters[shiftedPosition]

    print(f"Here is the {encode_or_decode}d result: {res}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))

    ceaser(txt=text, shft=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye!")