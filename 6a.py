from collections import defaultdict
import fileinput

for line in fileinput.input():
  seq = line.strip()

last_four = []
idx = 1
for char in seq:
  last_four.append(char)
  if len(last_four) > 4:
    last_four.pop(0)

  comp = defaultdict(int)
  for char in last_four:
    comp[char] += 1

  found = len(list(filter(lambda x: x == 1, comp.values()))) == 4
  if found:
    break
  idx += 1

print(idx)