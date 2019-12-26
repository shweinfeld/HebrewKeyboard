from graphics import*

"""This program creates a keyboard of hebrew charachters, allowing the user
to click on the desirable charachter and causing it to appear on the screen"""

win = GraphWin('Ivrit Keyboard', 600, 600)

def makeKeys (x, y, charachter):
    corner = Point(x, y)
    corner2 = corner.clone()
    corner2.move(30, 30)
    key = Rectangle(corner, corner2)
    key.draw(win)
    middle = corner.clone()
    middle.move(15, 15)
    letter = Text(middle, charachter)
    letter.draw(win)
    return (key, charachter)

def makeLine1(line1):
    keyList1 = []
    x = 513
    for charachter in line1:
        x = x-36
        y = 400
        keyList1.append(makeKeys(x, y, charachter))
    return keyList1

def makeLine2(line2):
    keyList2 = []
    x = 495
    for charachter in line2:
        x = x-36
        y = 436
        keyList2.append(makeKeys(x, y, charachter))
    return keyList2

def makeLine3(line3):
    keyList3 = []
    x = 477
    for charachter in line3:
        x = x-36
        y = 472
        keyList3.append(makeKeys(x, y, charachter))
    return keyList3


def makeSpacebar():
    corner = Point(407, 508)
    corner2 = corner.clone()
    corner2.move(-226, 30)
    spacebar = Rectangle(corner, corner2)
    spacebar.draw(win)
    charachter = ' ' u'\u200f' 
    return (spacebar, charachter)

def makeBackspace():
    corner = Point(175, 508)
    corner2 = corner.clone()
    corner2.move(-82, 30)
    backspace = Rectangle(corner, corner2)
    backspace.draw(win)
    middle = corner.clone()
    middle.move(-41, 15)
    symbol = Text(middle, u'\u2192')
    symbol.setSize(17)
    symbol.draw(win)
    return backspace

def makeEnter ():
    corner = Point(413, 508)
    corner2 = corner.clone()
    corner2.move(82, 30)
    enter = Rectangle(corner, corner2)
    enter.draw(win)
    middle = corner.clone()
    middle.move(41, 15)
    symbol = Text(middle, u'\u21B5')
    symbol.setSize(17)
    symbol.draw(win)
    charachter = '\n'
    return (enter, charachter)

def makeBase():
    corner = Point(513, 394)
    corner2 = corner.clone()
    corner2.move(-438, 150)
    base = Rectangle(corner, corner2)
    base.draw(win)

def makeCopy():
    corner = Point(594, 6)
    corner2 = corner.clone()
    corner2.move(-82, 30)
    copy = Rectangle(corner, corner2)
    copy.draw(win)
    middle = corner.clone()
    middle.move(-42, 15)
    symbol = Text(middle, 'Copy')
    symbol.draw(win)
    return copy

def makeKeyboard():
    keyList = []
    line1 = [u'\u05F3', u'\u05F4', u'\u05D0', u'\u05D1', u'\u05D2', u'\u05D3', u'\u05D4', u'\u05D5', u'\u05D6', u'\u05D7', '?' u'\u200f', '!' u'\u200f']
    line2 = [',' u'\u200f', u'\u05D8', u'\u05D9', u'\u05DB', u'\u05DA', u'\u05DC', u'\u05DE', u'\u05DD', u'\u05E0', u'\u05DF', u'\u05E1']
    line3 = ['.' u'\u200f', u'\u05E2', u'\u05E4', u'\u05E3', u'\u05E6', u'\u05E5', u'\u05E7', u'\u05E8', u'\u05E9', u'\u05EA']
  
    keyList.append(makeSpacebar())
    keyList.append(makeEnter())
    makeBase()
    keyList.extend(makeLine1(line1))
    keyList.extend(makeLine2(line2))
    keyList.extend(makeLine3(line3))
    return (keyList)


def inBetween(x, end1, end2):
    return end1 <= x <= end2 or end2<= x <= end1

def isInside(point, rect):
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return inBetween(point.getX(), pt1.getX(), pt2.getX()) and \
           inBetween(point.getY(), pt1.getY(), pt2.getY())

def userPick(List):
    letter = win.getMouse()
    for (key, charachter) in myKeyboard:
        if isInside(letter, key):
            List.append(charachter)
    if isInside(letter, backspace) and len(List) > 0:
        List.reverse()
        del List[0]
        List.reverse()
    jointList = ''.join(List)
    if isInside(letter, copy):#This merely copies the hebrew text to the python shell
        print(jointList)
    return jointList

def printLetter():
    letterList = []
    letter = userPick(letterList)
    sentence = Text(Point(win.getWidth()/2, 200), '')
    sentence.draw(win)
    while True:
        sentence.undraw()
        sentence = Text(Point(win.getWidth()/2, 200), letter)
        sentence.draw(win)
        letter = userPick(letterList)

backspace = makeBackspace()        
copy = makeCopy()         
myKeyboard = makeKeyboard()
printLetter()





    
        
