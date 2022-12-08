from collections import defaultdict
import fileinput

for line in fileinput.input():
  seq = line.strip()

last_fourteen = []
idx = 1
for char in seq:
  last_fourteen.append(char)
  if len(last_fourteen) > 14:
    last_fourteen.pop(0)

  comp = defaultdict(int)
  for char in last_fourteen:
    comp[char] += 1

  found = len(list(filter(lambda x: x == 1, comp.values()))) == 14
  if found:
    break
  idx += 1

print(idx)