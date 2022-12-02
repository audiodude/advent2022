import fileinput


def normalize(choice):
  if choice in ('A', 'X'):
    return 'R'

  if choice in ('B', 'Y'):
    return 'P'

  if choice in ('C', 'Z'):
    return 'S'


points = {
    'R': 1,
    'P': 2,
    'S': 3,
}

rotation = {
    'R': {
        'X': 'S',
        'Y': 'R',
        'Z': 'P'
    },
    'P': {
        'X': 'R',
        'Y': 'P',
        'Z': 'S'
    },
    'S': {
        'X': 'P',
        'Y': 'S',
        'Z': 'R'
    },
}

score = 0
for line in fileinput.input():
  left, right = line.strip().split(' ')

  score += points[rotation[normalize(left)][right]]

  if right == 'X':
    score += 0
  elif right == 'Y':
    score += 3
  elif right == 'Z':
    score += 6

print(score)