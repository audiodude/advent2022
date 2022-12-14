import fileinput

moves = []
for line in fileinput.input():
  line = line.strip()
  dir, n = line.split(' ')
  n = int(n)
  moves.append((dir, n))


def update_head(step, head):
  return (head[0] + step[0], head[1] + step[1])


def update_tail(head, tail):
  if head[0] == -8:
    print(head, tail)
  vector = (head[0] - tail[0], head[1] - tail[1])
  if vector[0] in (-1, 0, 1) and vector[1] in (-1, 0, 1):
    return tail

  for x in (-2, 2):
    if vector[0] == x:
      if vector[1] in (-2, 2):
        return (tail[0] + x // 2, tail[1] + vector[1] // 2)
      else:
        return (tail[0] + x // 2, tail[1] + vector[1])

  for y in (-2, 2):
    if vector[1] == y:
      if vector[0] in (-2, 2):
        return (tail[0] + vector[0] // 2, tail[1] + y // 2)
      else:
        return (tail[0] + vector[0], tail[1] + y // 2)

  raise ValueError(vector)


debug = False
snake = [(0, 0)] * 10
visited = set(snake[9:])
for move in moves:
  if move[0] == 'U':
    step = (0, -1)
  elif move[0] == 'D':
    step = (0, 1)
  elif move[0] == 'L':
    step = (-1, 0)
  elif move[0] == 'R':
    step = (1, 0)

  for _ in range(move[1]):
    snake[0] = update_head(step, snake[0])
    i = 1
    while i < len(snake):
      try:
        snake[i] = update_tail(snake[i - 1], snake[i])
      except ValueError:
        print(i, snake)
        raise
      i += 1
    print(snake)
    visited.add(snake[9])

print(len(visited))