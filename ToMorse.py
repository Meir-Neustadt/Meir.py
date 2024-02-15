morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",\
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",\
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",\
        "Y": "-.--", "Z": "--..", " ":"  "}

def IsLowerCase(i):
    return(i>='a' and i<='z')
def IsNotLetter(i):
    return((i<'A' or i>'Z')   and   (i<'a' or i>'z'))

def ToMorse(a):
    for i in a:
        if IsLowerCase(i):
            i=chr(ord(i)-32)
        if IsNotLetter(i) and i!=' ': 
            i=' '
        print(morse[i], end=' ')

a='Meir Neustadt Python'
ToMorse(a)
