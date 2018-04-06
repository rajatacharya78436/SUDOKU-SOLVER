import re
import random
import os
Sudoku_size = 81
def printSudoku (Sudoku, add_zeros):
  i = 0
  for val in Sudoku:
    if add_zeros == 1:
      if int(val) < 10: 
        print ('0'+str(val),)
      else:
        print (val,)
    else:
        print (val,)
    i +=1
    if i in [ (x*9)+3 for x in range(81)] +[ (x*9)+6 for x in range(81)] +[ (x*9)+9 for x in range(81)] :
        {print ('-----------')}
    if add_zeros == 1:
      if i in [ 27, 54, 81]:
        {print ('\n')}
      elif i in [ (x*9) for x in range(81)]:
        {print ('\n')}
    else:
      if i in [ 27, 54, 81]:
        {print ('\n')}
      elif i in [ (x*9) for x in range(81)]:
        {print ('*********************************************************************')}
def Full (Sudoku):
    return Sudoku.count('.') == 0
def get(Sudoku):
  for i in range(Sudoku_size):
    if Sudoku[i] == '.':
        return i
      
def Correct(trialVal, trialCelli, Sudoku):

  cols = 0
  for eachSq in range(9):
    trialSq = [ x+cols for x in range(3) ] + [ x+9+cols for x in range(3) ] + [ x+18+cols for x in range(3) ]
    cols +=3
    if cols in [9, 36]:
      cols +=18
    if trialCelli in trialSq:
      for i in trialSq:
        if Sudoku[i] != '.':
          if trialVal == int(Sudoku[i]):
                return False
  
  for eachRow in range(9):
    trialRow = [ x+(9*eachRow) for x in range (9) ]
    if trialCelli in trialRow:
      for i in trialRow:
        if Sudoku[i] != '.':
          if trialVal == int(Sudoku[i]):
                return False
  
  for eachCol in range(9):
    trialCol = [ (9*x)+eachCol for x in range (9) ]
    if trialCelli in trialCol:
      for i in trialCol:
        if Sudoku[i] != '.':
          if trialVal == int(Sudoku[i]):
                return False
  
  return True

def setCell(trialVal, trialCelli, Sudoku):
  Sudoku[trialCelli] = trialVal
  return Sudoku

def clearCell( trialCelli, Sudoku ):
  Sudoku[trialCelli] = '.'
  return Sudoku


def Solution (Sudoku):
  if Full(Sudoku):
    print ('\nSOLVED')
    return True
  else:
    trialCelli = get(Sudoku)
    trialVal = 1
    sol = False
    while ( sol != True) and (trialVal < 10):
      if Correct(trialVal, trialCelli, Sudoku):
        Sudoku = setCell(trialVal, trialCelli, Sudoku)
        if Solution (Sudoku) == True:
          sol = True
          return True
        else:
          clearCell( trialCelli, Sudoku )
      trialVal += 1
  return sol

def main ():
  #sampleSudoku = ['2', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '1', '.', '.', '.', '.', '9', '4', '.', '.', '.', '.', '7', '8', '2', '5', '.', '.', '4', '.', '.', '.', '.', '.', '.', '6', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '8', '2', '.', '.', '.', '7', '.', '.', '9', '.', '.', '.', '.', '.', '.', '.', '.', '3', '1', '.', '4', '.', '.', '.', '.', '.', '.', '.', '3', '8', '.']
  #sampleSudoku = ['.', '.', '3', '.', '2', '.', '6', '.', '.', '9', '.', '.', '3', '.', '5', '.', '.', '1', '.', '.', '1', '8', '.', '6', '4', '.', '.', '.', '.', '8', '1', '.', '2', '9', '.', '.', '7', '.', '.', '.', '.', '.', '.', '.', '8', '.', '.', '6', '7', '.', '8', '2', '.', '.', '.', '.', '2', '6', '.', '9', '5', '.', '.', '8', '.', '.', '2', '.', '3', '.', '.', '9', '.', '.', '5', '.', '1', '.', '3', '.', '.']
  sampleSudoku = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '6', '2', '9', '5', '1', '8', '1', '9', '6', '3', '5', '8', '2', '7', '4', '4', '7', '3', '8', '9', '2', '6', '5', '1', '6', '8', '.', '.', '3', '1', '.', '4', '.', '.', '.', '.', '.', '.', '.', '3', '8', '.']
  printSudoku(sampleSudoku, 0)
  if Solution (sampleSudoku):
    printSudoku(sampleSudoku, 0)
  else: print ('NO SOLUTION')

  
if __name__ == "__main__":
    main()

