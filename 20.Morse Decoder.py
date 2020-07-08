MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    code = code.split(' ')
    A = []
    for i in range(len(code)):
        if code[-i-1] == '' and code[-i-2] == '':
            A.append(-i-2)
    for i in A[::-1]:
        del code[i]
    for i in range(len(code)):
        if code[i] in MORSE:
            code[i] = MORSE[code[i]]
        else:
            code[i] = ' '
    code[0] = code[0].upper()
    return ''.join(code)
