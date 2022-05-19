notes = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}

intervals = {
  2:{
    0:'diminished',
    1:'minor',
    2:'Major',
    3:'augmented'
  },
  3:{
    2:'diminished',
    3:'minor',
    4:'Major',
    5:'augmented'
  },
  4:{
    4:'diminished',
    5:'perfect',
    6:'augmented'
  },
  5:{
    6:'diminished',
    7:'perfect',
    8:'augmented'
  },
  6:{
    7:'diminished',
    8:'minor',
    9:'Major',
    10:'augmented'
  },
  7:{
    9:'diminished',
    10:'minor',
    11:'Major',
    12:'augmented'
  }
}

fnote = input('first note: ').upper()
falt = input('0: natural \n1: sharp \n2: flat \nalteration: ')
snote = input('second note: ').upper()
salt = input('0: natural \n1: sharp \n2: flat \nalteration: ')
count = 0
result = 0
inter = 0

for x in notes:
  count += 1
  if x == fnote:
    fint = count
    fst = notes[x]
  if x == snote:
    sint = count
    sst = notes[x]

if falt == '1':
  fst += 1
elif falt == '2':
  fst -= 1
if salt == '1':
  sst += 1
elif salt == '2':
  sst -= 1

if fint >= sint:
  result = fint - sint
  intVal = result + 1
  if intVal == 2:
    numerator = 'nd'
  elif intVal == 3:
    numerator = 'rd'
  else:
    numerator = 'th'
  inter = fst - sst
  for x in intervals:
    if intVal == x:
      for y in intervals[x]:
        if inter == y:
          print(intervals[x][y], str(intVal) + numerator)
else:
  result = sint - fint
  intVal = result + 1
  if intVal == 2:
    numerator = 'nd'
  elif intVal == 3:
    numerator = 'rd'
  else:
    numerator = 'th'

  inter = sst - fst
  for x in intervals:
    if intVal == x:
      for y in intervals[x]:
        if inter == y:
          print(intervals[x][y], str(intVal) + numerator)
