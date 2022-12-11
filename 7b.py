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


def smallest_freeing_child(node, n, stash=None):
  cur_size = walk(node, sum)
  if stash is None:
    stash = {'node': node, 'size': cur_size}
  if cur_size >= n and cur_size < stash['size']:
    stash['node'] = node
    stash['size'] = cur_size

  for dir in node.dirs:
    smallest_freeing_child(dir, n, stash)
  return stash


to_free = walk(root, sum) - 40000000
print(smallest_freeing_child(root, to_free)['size'])
