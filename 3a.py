import fileinput


def find_common(first, second):
  first = sorted(list(first))
  second = sorted(list(second))

  next_first = first.pop(0)
  next_second = second.pop(0)
  while True:
    if next_first == next_second:
      return next_first

    while next_first < next_second:
      next_first = first.pop(0)
      continue

    while next_second < next_first:
      next_second = second.pop(0)
      continue


total = 0
for line in fileinput.input():
  line = line.strip()
  half = len(line) // 2
  first, second = line[:half], line[half:]

  item = find_common(first, second)

  if item.lower() == item:
    total += ord(item) - 96
  else:
    total += ord(item) - 38

print(total)
