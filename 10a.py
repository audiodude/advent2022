import fileinput


def add_strength():
  for epoch in epochs:
    if n == epoch:
      return epoch * x
  return 0


x = 1
n = 1
strength = 0
epochs = (20, 60, 100, 140, 180, 220)
for line in fileinput.input():
  line = line.strip()

  if line.startswith('noop'):
    n += 1
    strength += add_strength()
    continue

  instr, p = line.split(' ')
  p = int(p)

  n += 1
  strength += add_strength()
  x += p
  n += 1
  strength += add_strength()

print(strength)