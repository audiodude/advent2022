import fileinput


def normalize(choice):
  if choice in ('A', 'X'):
    return 'R'

  if choice in ('B', 'Y'):
    return 'P'

  if choice in ('C', 'Z'):
    return 'S'


def beats(a, b):
  if a == 'R':
    return b == 'S'

  if a == 'P':
    return b == 'R'

  if a == 'S':
    return b == 'P'


score = 0
for line in fileinput.input():
  left, right = line.strip().split(' ')
  left, right = normalize(left), normalize(right)

  if beats(left, right):
    score += 0
  elif beats(right, left):
    score += 6
  else:
    score += 3

  if right == 'R':
    score += 1
  elif right == 'P':
    score += 2
  elif right == 'S':
    score += 3

print(score)