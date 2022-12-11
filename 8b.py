import fileinput

trees = []
for line in fileinput.input():
  trees.append(list(int(tree) for tree in line.strip()))


def left(x, y):
  return [(i, y) for i in range(x - 1, -1, -1)]


def right(x, y):
  return [(i, y) for i in range(x + 1, len(trees[y]))]


def up(x, y):
  return [(x, i) for i in range(y - 1, -1, -1)]


def down(x, y):
  return [(x, i) for i in range(y + 1, len(trees))]


def scored(x, y, height):
  score = 1
  for it in (left(x, y), right(x, y), up(x, y), down(x, y)):
    count = 0
    for x, y in it:
      count += 1
      if trees[y][x] >= height:
        break
    score *= count
  return score


m = None
for y in range(len(trees)):
  for x in range(len(trees[0])):
    score = scored(x, y, trees[y][x])
    if m is None or score > m:
      m = score

print(m)