import sys
from functools import cmp_to_key
from math import gcd


class Node:
	__slots__ = ('seg', 'prio', 'left', 'right', 'parent')

	def __init__(self, seg):
		self.seg = seg
		self.prio = ((seg + 1) * 1103515245 + 12345) & 0x7fffffff
		self.left = None
		self.right = None
		self.parent = None


def normalize(x, y):
	g = gcd(abs(x), abs(y))
	return (x // g, y // g)


def angle_cmp(a, b):
	ax, ay = a
	bx, by = b
	ha = 0 if (ay > 0 or (ay == 0 and ax > 0)) else 1
	hb = 0 if (by > 0 or (by == 0 and bx > 0)) else 1
	if ha != hb:
		return -1 if ha < hb else 1
	cross = ax * by - ay * bx
	if cross > 0:
		return -1
	if cross < 0:
		return 1
	return 0


def ray_key(seg, vx, vy):
	sx, sy, ex, ey = seg
	dx = ex - sx
	dy = ey - sy
	num = sx * dy - sy * dx
	den = vx * dy - vy * dx
	if den < 0:
		num = -num
		den = -den
	return num, den


def closer(seg_a, seg_b, vx, vy):
	a_num, a_den = ray_key(seg_a, vx, vy)
	b_num, b_den = ray_key(seg_b, vx, vy)
	return a_num * b_den < b_num * a_den


def rotate_left(root, x):
	y = x.right
	x.right = y.left
	if y.left is not None:
		y.left.parent = x
	y.parent = x.parent
	if x.parent is None:
		root = y
	elif x.parent.left is x:
		x.parent.left = y
	else:
		x.parent.right = y
	y.left = x
	x.parent = y
	return root


def rotate_right(root, x):
	y = x.left
	x.left = y.right
	if y.right is not None:
		y.right.parent = x
	y.parent = x.parent
	if x.parent is None:
		root = y
	elif x.parent.left is x:
		x.parent.left = y
	else:
		x.parent.right = y
	y.right = x
	x.parent = y
	return root


def insert(root, node, vx, vy, segments):
	node.left = node.right = node.parent = None
	if root is None:
		return node

	cur = root
	while True:
		if closer(segments[node.seg], segments[cur.seg], vx, vy):
			if cur.left is None:
				cur.left = node
				node.parent = cur
				break
			cur = cur.left
		else:
			if cur.right is None:
				cur.right = node
				node.parent = cur
				break
			cur = cur.right

	while node.parent is not None and node.prio < node.parent.prio:
		if node.parent.left is node:
			root = rotate_right(root, node.parent)
		else:
			root = rotate_left(root, node.parent)
	return root


def remove(root, node):
	while node.left is not None and node.right is not None:
		if node.left.prio < node.right.prio:
			root = rotate_right(root, node)
		else:
			root = rotate_left(root, node)

	child = node.left if node.left is not None else node.right
	if node.parent is None:
		root = child
		if child is not None:
			child.parent = None
	else:
		if node.parent.left is node:
			node.parent.left = child
		else:
			node.parent.right = child
		if child is not None:
			child.parent = node.parent

	node.left = node.right = node.parent = None
	return root


def leftmost(root):
	if root is None:
		return None
	while root.left is not None:
		root = root.left
	return root


def sample_vector(a, b):
	ax, ay = a
	bx, by = b
	cross = ax * by - ay * bx
	if cross > 0:
		return ax + bx, ay + by
	if cross < 0:
		return -(ax + bx), -(ay + by)
	return -ay, ax


def solve_case(n, raw_segments):
	segments = []
	dirs = []
	for sx, sy, ex, ey in raw_segments:
		p = normalize(sx, sy)
		q = normalize(ex, ey)
		dirs.append(p)
		dirs.append(q)
		segments.append((sx, sy, ex, ey, p, q))

	unique_dirs = sorted(set(dirs), key=cmp_to_key(angle_cmp))
	if len(unique_dirs) < 2:
		return [0] * n

	dir_index = {d: i for i, d in enumerate(unique_dirs)}
	k = len(unique_dirs)

	starts = [[] for _ in range(k)]
	ends = [[] for _ in range(k)]
	nodes = [Node(i) for i in range(n)]
	visible = [0] * n
	active = [False] * n

	for i, (sx, sy, ex, ey, p, q) in enumerate(segments):
		sp = dir_index[p]
		ep = dir_index[q]
		cross = p[0] * q[1] - p[1] * q[0]
		if cross > 0:
			start, end = sp, ep
		elif cross < 0:
			start, end = ep, sp
		else:
			# Zero angular width; ignored under the open-interval visibility model.
			continue

		starts[start].append(i)
		ends[end].append(i)
		if start > end:
			active[i] = True

	root = None
	vx0, vy0 = sample_vector(unique_dirs[-1], unique_dirs[0])
	for i in range(n):
		if active[i]:
			root = insert(root, nodes[i], vx0, vy0, segments)

	for i in range(k):
		for sid in ends[i]:
			if active[sid]:
				root = remove(root, nodes[sid])
				active[sid] = False

		vx, vy = sample_vector(unique_dirs[i], unique_dirs[(i + 1) % k])

		for sid in starts[i]:
			if not active[sid]:
				root = insert(root, nodes[sid], vx, vy, segments)
				active[sid] = True

		front = leftmost(root)
		if front is not None:
			visible[front.seg] = 1

	return visible


def main():
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	out = []
	idx = 0
	total = len(data)
	while idx < total:
		n = data[idx]
		idx += 1
		if idx + 4 * n > total:
			break
		raw_segments = []
		for _ in range(n):
			raw_segments.append(tuple(data[idx:idx + 4]))
			idx += 4
		ans = solve_case(n, raw_segments)
		out.append(' '.join(map(str, ans)))

	sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
	main()

