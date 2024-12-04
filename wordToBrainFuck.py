letters = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','\'',',','.','!','?','+','-','[',']','>','<']
word = list('')
elements = []
for i in range(len(word)):
    elements.append(letters.index(word[i]))
print(elements)
elements2 = []
for i in range(len(elements)):
    for z in range(elements[i]):
        elements2.append('+')
    elements2.append('.')
    elements2.append('[')
    elements2.append('-')
    elements2.append(']')
print(elements2)
elementsString = ''
for i in range(len(elements2)):
    elementsString = elementsString + str(elements2[i])
print(elementsString)    
