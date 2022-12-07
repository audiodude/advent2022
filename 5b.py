from collections import defaultdict
import fileinput


def process_crates():
  indices = raw_crates.pop()
  *_, highest = map(int, filter(lambda x: x != '', indices.split(' ')))

  crates = defaultdict(list)
  for line in reversed(raw_crates):
    for c, i in zip(range(1, highest + 1), range(1, (highest * 4) - 2, 4)):
      crate = line[i] if i < len(line) else ' '
      if crate != ' ':
        crates[c].append(line[i])

  return crates


moves = []
raw_crates = []
reading_crates = True
for line in fileinput.input():
  line = line.strip('\n')
  if reading_crates:
    if line == '':
      reading_crates = False
      continue
    raw_crates.append(line)
    continue

  move = line.split(' ')
  moves.append(tuple(map(int, move[1::2])))

crates = process_crates()

for num, src, dest in moves:
  crates[dest].extend(crates[src][-1 * num:])
  crates[src] = crates[src][:-1 * num]

ans = ''
for _, crate in crates.items():
  ans += crate.pop()

print(ans)