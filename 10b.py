import fileinput


def print_char():
  pos = (n - 1) % 40
  if pos == 0:
    print()
  if pos - x in (-1, 0, 1):
    print('#', end='')
  else:
    print('.', end='')


x = 1
n = 1
strength = 0
print_char()
for line in fileinput.input():
  line = line.strip()

  if line.startswith('noop'):
    n += 1
    print_char()
    continue

  instr, p = line.split(' ')
  p = int(p)

  n += 1
  print_char()
  x += p
  n += 1
  print_char()
