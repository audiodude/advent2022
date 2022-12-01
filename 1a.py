import fileinput

cur = 0
totals = []
for line in fileinput.input():
  n = line.strip()
  if n == '':
    totals.append(cur)
    cur = 0
  else:
    cur += int(n)
totals.append(cur)

print(max(totals))