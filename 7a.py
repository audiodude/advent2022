from collections import namedtuple
import fileinput

Node = namedtuple('Node', 'name dirs files parent')
cwd = Node('/', [], [], None)
root = cwd
for line in fileinput.input():
  line = line.strip()
  if line.startswith('$'):
    if line[2:4] == 'cd':
      next_name = line[5:]
      if next_name == '..':
        cwd = cwd.parent
        continue
      elif next_name == '/':
        continue
      cwd = next(dir for dir in cwd.dirs if dir.name == next_name)
      continue
    if line[2:4] == 'ls':
      continue
  if line.startswith('dir'):
    cwd.dirs.append(Node(line[4:], [], [], cwd))
  else:
    cwd.files.append(int(line.split(' ')[0]))


def walk(node, fn):
  return fn(node.files) + fn(walk(dir, fn) for dir in node.dirs)


def sizes_lte(node, n, stash=None):
  if stash is None:
    stash = []
  size = walk(node, sum)
  if size <= 100000:
    stash.append(size)
  for dir in node.dirs:
    sizes_lte(dir, n, stash)
  return stash


print(sum(sizes_lte(root, 100000)))
