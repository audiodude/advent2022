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


head = tail = (0, 0)
visited = set((tail,))
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
    head = update_head(step, head)
    tail = update_tail(head, tail)
    visited.add(tail)

print(len(visited))