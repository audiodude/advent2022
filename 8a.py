import fileinput

trees = []
for line in fileinput.input():
  trees.append(list(int(tree) for tree in line.strip()))


def visible(line, x=None, y=None, reverse=False):
  if reverse:
    it = zip(range(len(line) - 1, -1, -1), reversed(line))
  else:
    it = enumerate(line)

  coords = set()
  max = None
  for i, tree in it:
    if max is None or tree > max:
      max = tree
      if i != 0 and i != len(line) - 1:
        if x is None:
          coords.add((i, y, tree))
        else:
          coords.add((x, i, tree))
  return coords


count = len(trees) * 2 + (len(trees[0]) - 2) * 2
coords = set()
for y, row in enumerate(trees):
  if y == 0 or y == len(trees) - 1:
    continue
  for reverse in (True, False):
    coords |= visible(row, y=y, reverse=reverse)

for x in range(len(trees[0])):
  if x == 0 or x == len(trees[0]) - 1:
    continue
  col = list(trees[y][x] for y in range(len(trees)))
  for reverse in (True, False):
    coords |= visible(col, x=x, reverse=reverse)

print(count + len(coords))