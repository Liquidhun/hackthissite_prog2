from PIL import Image
'''
https://www.hackthissite.org/missions/prog/2/

The pixels in the above image are numbered 0..99 for the first row, 100..199 for the second row etc. 
White pixels represent ascii codes. 
The ascii code for a particular white pixel is equal to the offset from the last white pixel. 
For example, the first white pixel at location 65 would represent ascii code 65 ('A'), 
the next at location 131 would represent ascii code (131 - 65) = 66 ('B') and so on.

The text contained in the image is the answer encoded in Morse, where "a test" would be encoded as ".- / - . ... -"
'''

pic = "PNG.png"
pix = Image.open(pic)
rgb_im = pix.convert('RGB')
[width, height] = pix.size
preposition = 0
ascii = []
morse = ""
answer = ""

MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y':
        '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '/': '-..-.', '(': '-.--.-',
    ')': '-.--.-', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '': ''
}

def findLetter(morse_code):
    for k, v in MORSE_DICT.items():
        if v == morse_code:
            return k

for h in range(0, height, 1):
    for w in range(0, width, 1):
                r, g, b = rgb_im.getpixel((w, h))
                if "".join(str(r)+str(g)+str(b)) != "000":
                    ascii.append(w + h * 100 - preposition)
                    preposition = w + h * 100
strng = ""
for i in range(len(ascii)):
    strng += str(chr(ascii[i]))

final = strng.split(" ")

for i in range(len((final))):
    answer+= str(findLetter(final[i]))

print (answer)
print ("\n")