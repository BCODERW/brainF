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
        print(Print)
    returnList = []
    returnList.append(cells)
    returnList.append(selected)
    returnList.append(Print)
    return returnList
sel = 0
success = False
print('Output 3 in cell 1')
#answer(effecient) +++
while not success:
    myCode = list(input('Enter your brainF*** code here: '))
    codeRan = mainCode(myCode,cells,sel)
    print('Your output: ')
    print(codeRan[0])
    cells = codeRan[0]
    sel = codeRan[1]
    if(cells[0] == 3):
        success = True
    else:
        print('You failed, try again')
        cells = [0,0,0,0,0,0,0,0,0,0]
        sel = 0
print('You did it! On to the next one')
print('Precondition: cell 1 is set to 5')
print('With only 3 characters, set cell 1 to 0')
#answer [-]
sel = 0
success = False
while not success:
    cells[0] = 5
    myCode = list(input('Enter your brainF*** code here: '))
    if len(myCode) == 3:
        codeRan = mainCode(myCode,cells,sel)
        print('Your output: ')
        print(codeRan[0])
        cells = codeRan[0]
        sel = codeRan[1]
        if cells[0] == 0:
            success = True
        else:
            print('You failed, try again')
            sel = 0
            cells = [5,0,0,0,0,0,0,0,0,0]
    else:
        print('It needs to have 3 characters only, try again')
        sel = 0
        cells = [5,0,0,0,0,0,0,0,0,0]
print('')
print('You did it again! Get ready for the next one')
print('This one is very similar to the previous, but every cell has a value of 5, and you only get 4 characters to get them all to 0')
#answer [->]
sel = 0
success = False
while not success:
    for i in range(10):
        cells[i] = 5
    myCode = list(input('Enter your brainF*** code here: '))
    if len(myCode) == 4:
        codeRan = mainCode(myCode,cells,sel)
        print('Your output: ')
        print(codeRan[0])
        cells = codeRan[0]
        sel = codeRan[1]
        success = True
        for i in range(10):
            if cells[i] != 0:
                success = False
        if not success:
            cells = [5,5,5,5,5,5,5,5,5,5]
            print('You failed, try again')
            sel = 0
    else:
        print('It needs to have 4 characters only, try again')
        sel = 0
        cells = [5,5,5,5,5,5,5,5,5,5]
print('Amazing! If you don\'t have any experience with brainF*** then you are entering the challenge section')
print('Get cell 1 to contain the number 100 with less than 50 characters')
#answer ++++++++++[->++++++++++<]>[-<+>] - 32 characters
sel = 0
success = False
while not success:
    for i in range(10):
        cells[i] = 0
    myCode = list(input('Enter your brainF*** code here: '))
    if len(myCode) < 50:
        codeRan = mainCode(myCode,cells,sel)
        print('Your output: ')
        print(codeRan[0])
        cells = codeRan[0]
        sel = codeRan[1]
        if cells[0] == 100:
            success = True
        else:
            print('You failed, try again')
            sel = 0
            cells = [0,0,0,0,0,0,0,0,0,0]
    else:
        print('It needs to have less than 50 characters only, try again')
        sel = 0
        cells = [0,0,0,0,0,0,0,0,0,0]
print('Impressive, now on to the final tasks. Usually you need to know the ascii values to output characters. For this a is 1, b is 2, ..., z is 26')
print('Say hi')
#an answer ++++++++.[-]+++++++++.[-]
sel = 0
success = False
while not success:
    for i in range(10):
        cells[i] = 0
    myCode = list(input('Enter your brainF*** code here: '))
    if len(myCode) >= 0:
        codeRan = mainCode(myCode,cells,sel)
        print('Your output: ')
        print(codeRan[0])
        cells = codeRan[0]
        sel = codeRan[1]
        Print = codeRan[2]
        if Print == 'hi':
            success = True
        else:
            print('Not quite, please try again')
            sel = 0
            cells = [0,0,0,0,0,0,0,0,0,0]
    else:
        print('Uh oh I havent seen any code that bad, ever')
print('You need to output a program, that if run would have 81 in the first cell. You may output no more than 80 characters, but the progrm you input has no character limit. + is 68, - 69, [ 70, ] 71, > 72, < 73, . 74')
sel = 0
success = False
while not success:
    for i in range(10):
        cells[i] = 0
    myCode = list(input('Enter your brainF*** code here: '))
    codeRan = mainCode(myCode,cells,sel)
    print('Your output: ')
    print(codeRan[0])
    cells = codeRan[0]
    sel = codeRan[1]
    Print = codeRan[2]
    if(len(list(Print)) < 81):
        if(mainCode(Print,[0,0,0,0,0,0,0,0,0,0],0)[0][0] == 81):
            success = True
        else:
            print('Not quite, but what do you expect, it\'s pretty dang difficult')
            sel = 0
            cells = [0,0,0,0,0,0,0,0,0,0]
    else:
        print('The printed code had 81 or more characters. The printed code can be at most 80 characters. Try again!')
        sel = 0
        cells = [0,0,0,0,0,0,0,0,0,0]
print('Amazing! If you did this without any converting script, I can\'t imagine the dedication you have')
