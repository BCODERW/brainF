cells = []
for i in range(10):
    cells.append(0)

    
def mainCode(code,cells,selected):
    output = []
    letters = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','\'',',','.','!','?','+','-','[',']','>','<']
#               0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17 18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52   53  54 55  56   57  58  59 60  61  62  63   64  65  66  67  68  69  70  71  72  73
    #print(cells)
    i = 0
    while i < len(code):
        if code[i] == '+':
            cells[selected] += 1

        if code[i] == '-':
            if cells[selected] > 0:
                cells[selected] -= 1

        if code[i] == '>':
            
            if selected != 9:
                selected += 1

            else:
                selected = 0

        if code[i] == '<':

            if selected != 0:
                selected -= 1

            else:
                selected = 9

        if code[i] == '.':
            output.append(letters[cells[selected]])
        if code[i] == '[':
            count = 1
            inLoop = []
            loopingIndex = i + 1
            while count != 0:
                if code[loopingIndex] == '[':
                    count += 1
                    #print('inc')

                if code[loopingIndex] == ']':
                    count -= 1
                    #print('dec')
                    
                inLoop.append(code[loopingIndex])
                loopingIndex += 1
                
            del inLoop[len(inLoop)-1]
            
            while cells[selected] != 0:
                #print(cells[selected])
                #print('Doing loop')
                #print(len(inLoop))
                #print(inLoop)
                returned = mainCode(inLoop,cells,selected)
                cells = returned[0]
                selected = int(returned[1])
            i += len(inLoop)
        i += 1
    Print = ""
    if output != []:
        for i in range(len(output)):
            Print += output[i]
        print('Your word output: ')
        print(Print)
    returnList = []
    returnList.append(cells)
    returnList.append(selected)
    returnList.append(Print)
    return returnList
sel = 0
while True:
  myCode = list(input('Enter your brainFuck code here: '))
  print('Your output: ')
  print(codeRan[0])
  cells = codeRan[0]
  sel = codeRan[1]
                
