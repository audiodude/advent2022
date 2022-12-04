import fileinput


def find_common(group):
  first = sorted(list(group[0]))
  second = sorted(list(group[1]))
  third = sorted(list(group[2]))

  next_first = first.pop(0)
  next_second = second.pop(0)
  next_third = third.pop(0)
  while True:
    if next_first == next_second == next_third:
      return next_first

    while next_first < next_second or next_first < next_third:
      next_first = first.pop(0)
      continue

    while next_second < next_first or next_second < next_third:
      next_second = second.pop(0)
      continue

    while next_third < next_first or next_third < next_second:
      next_third = third.pop(0)
      continue


total = 0
group = []
n = 0
for line in fileinput.input():
  line = line.strip()
  group.append(line)
  n += 1
  if n % 3 == 0:
    item = find_common(group)
    group = []
  else:
    continue

  if item.lower() == item:
    total += ord(item) - 96
  else:
    total += ord(item) - 38

print(total)
