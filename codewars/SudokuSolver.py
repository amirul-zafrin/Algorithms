import numpy as np

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

removeVal = lambda list1, list2: list(filter(lambda element: element not in list2, list1))
maintainDup = lambda list1, list2: list(filter(lambda element: element in list2, list1))

def sudoku(puzzle):
    pzl = np.array(puzzle)
    posDict, posLen = possibleVal(pzl)
    while 1 in posLen.values():
        for (r,c,b), value in posLen.items():
            if value == 1:
                pzl[r,c] = posDict[r,c,b][0]
                posDict, posLen = updatePosVal(posDict, posLen, (r,c,b), posDict[r,c,b][0])
            else:
                lst = uniqueRCB(posDict, posLen, (r,c,b))
                posDict[r,c,b] = lst
                posLen[r,c,b] = len(lst)
                
        posLen = {k: v for k, v in posLen.items() if v != 0}
        lst = [ k for k, v in posLen.items() if v != 0]
        posDict = {k: v for k, v in posDict.items() if k in lst}

    return pzl

def uniqueRCB(posDict : dict, posLen : dict, pos : tuple) -> list:
    unique = []
    row,col,box = pos
    for (r,c,b), value in posDict.items():
        if r == row or c == col or b == box:
            unique.extend(value)
    unique = list(set(unique))
    res = maintainDup(posDict[pos],unique)

    if len(res) == 0:
        res = posDict[pos]
    return res 

def checkPosRC(puzzle) -> dict:
    row = {}
    col = {}
    for x in range(0,9):
        row[x] = removeVal(list(range(1,10)),puzzle[x])
        for y in range(0,9):
            if col.get(y) is None:
                col[y] = [puzzle[x,y]]
            else: 
                col[y].append(puzzle[x,y])
    for key, value in col.items():
        col[key] = removeVal(list(range(1,10)),value)
    
    return row, col

def checkPosBox(puzzle) -> dict:
    lmt = [3,6,9]
    dct = {}
    for x in lmt:
        for y in lmt:
            lst = puzzle[x-3:x,y-3:y].flatten().tolist()
            dct[int(x-3+(y/3))] = removeVal(list(range(1,10)),lst)
    return dct

def whichBox(x,y) -> int:
    return int(y/3) + 1 + (int(x/3)*3)

def possibleVal(puzzle) -> dict:
    rowPos, colPos = checkPosRC(puzzle)
    boxPos = checkPosBox(puzzle)
    posDict = {}
    posLen = {}
    for x in range(9):
        for y in range(9):
            if puzzle[x,y] == 0:
                box = whichBox(x, y)
                lst = maintainDup(rowPos[x],colPos[y])
                pos = maintainDup(lst,boxPos[box])
                posDict[(x,y,box)] = list(set(pos))
                posLen[(x,y,box)] = len(set(pos))
    return posDict, posLen

def updatePosVal(posDict:dict, posLen: dict, pos:tuple, value:int) -> dict:
    for (r,c,b) in posDict:
        if (r == pos[0] or c == pos[1]) or b == pos[2]:
            if value in posDict[r,c,b]:
                posDict[r,c,b].remove(value)
                posLen[r,c,b] -= 1
                    
    return posDict, posLen

def display(puzzle):
    for x in range(1,10):
        st = ""
        for y in range(1,10):
            st += f"  {puzzle[x-1,y-1]}  "
            if y % 3 == 0 and y != 9:
              st += "|"  

        print(st)
        if x % 3 == 0 and x != 9:
            print("---------------+---------------+---------------")