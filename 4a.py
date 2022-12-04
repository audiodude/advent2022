import fileinput


def to_tuple(chunk):
  return tuple(int(x) for x in chunk.split('-'))


def overlaps_completely(left, right):
  return (left == right or (left[0] <= right[0] and left[1] >= right[1]) or
          (right[0] <= left[0] and right[1] >= left[1]))


count = 0
for line in fileinput.input():
  left, right = line.strip().split(',')
  left = to_tuple(left)
  right = to_tuple(right)
  count += 1 if overlaps_completely(left, right) else 0

print(count)