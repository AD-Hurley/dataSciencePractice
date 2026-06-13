def TiangleArea(base, height, shape='triangle'):
    if shape == 'rectangle':
        return base * height
    else:
        return 0.5 * base * height

def printPattern(rows):
    starStr=''
    for i in range(rows):
        starStr=starStr+'*'
        print(starStr)

print(TiangleArea(3,4,'rectangle'))

printPattern(5)