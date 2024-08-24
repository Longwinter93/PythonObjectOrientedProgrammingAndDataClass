#A mapping table saved as dictionary 
mapping = {
            'A':'A',
            'B':'B',
            'C':'C',
            'D':'D',
            'E':'E',
            'F':'F',
            'Z':'Z',
            'G':'G',
            'H':'H',
            'I':'I',
            'K':'K',
            'L':'L',
            'M':'M',
            'N':'N',
            'U':'U',
            'O':'O',
            'P':'P',
            'Q':'Q',
            'R':'R',
            'S':'S',
            'T':'T',
            'V':'V',
            'X':'X',
            'a':'a',
            'b':'b',
            'c':'c',
            'd':'d',
            'e':'e',
            'f':'f',
            'z':'z',
            'g':'g',
            'h':'h',
            'i':'i',
            'k':'k',
            'l':'l',
            'm':'m',
            'n':'n',
            'o':'o',
            'p':'p',
            'q':'q',
            'r':'r',
            'u':'u',
            's':'s',
            't':'t',
            'v':'v',
            'x':'x',
            '1':'1',
            '2':'2',
            '3':'3',
            '4':'4',
            '5':'5',
            '6':'6',
            '7':'7',
            '8':'8',
            '9':'9',
            '0':'0',
            '.':'.'}

#variables hold strings
a = 'O’Connor'
b= 'Tristan�'
c = 'Łukasz'
d = ' Дмитро́'


#First function
def convertedFunctionLoop(word):
    newlist = []
    for letter in word:
        convertedwords = mapping.get(letter,'')
        newlist.append(convertedwords)
        convertedwords= list(filter(None,newlist))
        convertedwords= ''.join(convertedwords)
        convertedwords = convertedwords.strip()
    return convertedwords
        

print(convertedFunctionLoop(a))
print(convertedFunctionLoop(b))
print(convertedFunctionLoop(c))    
print(convertedFunctionLoop(d)) 

#Second Function
def convertedString(words):
    convertedCharacter = [mapping.get(char,' ') for char in words]
    convertedCharacter = list(filter(None, convertedCharacter))
    convertedCharacter = ''.join(convertedCharacter)
    convertedCharacter = convertedCharacter.strip()
    
    return convertedCharacter 

print(convertedString(a))
print(convertedString(b))
print(convertedString(c))
print(convertedString(d))

