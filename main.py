

word = 'abstrait'

def createBoolList(w) :
  list = []
  for c in w:
    list.append(False)
  return list

boolList = createBoolList(word)
tries = 7

triedLetters = []

while (tries > 0) and (False in boolList):
  letter = input('which letter\n')
  if letter in word and not letter in triedLetters:
    i = 0
    for c in word:
      if letter == c:
        boolList[i] = True
      i += 1
  else:
    tries -= 1
  
  if not letter in triedLetters:
      triedLetters.append(letter)

  print (boolList)
  print (' ' + str(tries) + '\n')
  print (triedLetters)
