import sys
from fractions import Fraction as F


def merge_len(segs):
	if not segs:
		return F(0)
	segs.sort()
	s = F(0)
	l, r = segs[0]
	for a, b in segs[1:]:
		if a > r:
			s += r - l
			l, r = a, b
		elif b > r:
			r = b
	return s + (r - l)


def main():
	a = list(map(int, sys.stdin.buffer.read().split()))
	if not a:
		return
	n, w, T, V = a[:4]
	x, L, v = [F(0)] * n, [0] * n, [0] * n
	p = 4
	for i in range(n):
		x[i], L[i], v[i] = F(a[p]), a[p + 1], a[p + 2]
		p += 3

	W, T = F(w), F(T)
	if T == 0:
		print("0.00")
		return

	def hit_dt(i):
		if v[i] == 0 or L[i] == w:
			return None
		if v[i] > 0:
			return (W - L[i] - x[i]) / v[i]
		return x[i] / (-v[i])

	area = F(0)
	t = F(0)
	while t < T:
		dts = [d for i in range(n) if (d := hit_dt(i)) is not None and d > 0]
		dt = min(dts) if dts else (T - t)
		if t + dt > T:
			dt = T - t

		t0, t1 = t, t + dt
		x0, v0 = x[:], v[:]

		# In [t0,t1], all umbrellas move linearly with fixed velocity.
		events = {t0, t1}
		ends = []
		for i in range(n):
			s = F(v0[i])
			c = x0[i] - s * t0
			ends.append((c, s))
			ends.append((c + L[i], s))
		m = len(ends)
		for i in range(m):
			c1, s1 = ends[i]
			for j in range(i + 1, m):
				c2, s2 = ends[j]
				if s1 == s2:
					continue
				tc = (c2 - c1) / (s1 - s2)
				if t0 < tc < t1:
					events.add(tc)

		ts = sorted(events)
		for i in range(len(ts) - 1):
			a0, b0 = ts[i], ts[i + 1]
			seg_a, seg_b = [], []
			da, db = a0 - t0, b0 - t0
			for k in range(n):
				la = x0[k] + F(v0[k]) * da
				lb = x0[k] + F(v0[k]) * db
				ra, rb = la + L[k], lb + L[k]
				if ra > 0 and la < W:
					seg_a.append((max(la, F(0)), min(ra, W)))
				if rb > 0 and lb < W:
					seg_b.append((max(lb, F(0)), min(rb, W)))
			ca = merge_len(seg_a)
			cb = merge_len(seg_b)
			area += (b0 - a0) * (ca + cb) / 2

		for i in range(n):
			x[i] += F(v[i]) * dt
		t = t1
		if t == T:
			break
		for i in range(n):
			d = hit_dt(i)
			if d is not None and d == 0:
				v[i] = -v[i]

	rain = (W * T - area) * V
	print(f"{float(rain):.2f}")


if __name__ == "__main__":
	main()
