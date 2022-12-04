import fileinput


def to_tuple(chunk):
  return tuple(int(x) for x in chunk.split('-'))


def overlaps(left, right):
  left_overlaps = left[0] <= right[0] and right[0] <= left[1]
  right_overlaps = right[0] <= left[0] and left[0] <= right[1]

  return (left == right or left_overlaps or right_overlaps)


count = 0
for line in fileinput.input():
  left, right = line.strip().split(',')
  left = to_tuple(left)
  right = to_tuple(right)
  count += 1 if overlaps(left, right) else 0

print(count)