import sys
from fractions import Fraction


def main() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	p = 0
	n, w, t_end, rain_v = data[p], data[p + 1], data[p + 2], data[p + 3]
	p += 4

	x = [Fraction(0) for _ in range(n)]
	l = [0] * n
	v = [0] * n
	for i in range(n):
		x[i], l[i], v[i] = Fraction(data[p]), data[p + 1], data[p + 2]
		p += 3

	if t_end == 0:
		print("0.00")
		return

	T = Fraction(t_end)
	W = Fraction(w)

	def time_to_wall(i: int):
		if v[i] == 0 or l[i] == w:
			return None
		if v[i] > 0:
			d = Fraction(w - l[i]) - x[i]
			return d / v[i] if d >= 0 else Fraction(0)
		d = x[i]
		return d / (-v[i]) if d >= 0 else Fraction(0)

	# Build global time blocks where every umbrella has constant velocity.
	blocks = []
	t = Fraction(0)
	while t < T:
		dts = []
		for i in range(n):
			dt = time_to_wall(i)
			if dt is not None and dt > 0:
				dts.append(dt)
		dt = min(dts) if dts else (T - t)
		if t + dt > T:
			dt = T - t

		x0 = x[:]
		v0 = v[:]
		t0, t1 = t, t + dt
		blocks.append((t0, t1, x0, v0))

		for i in range(n):
			x[i] = x[i] + Fraction(v[i]) * dt
		t = t1
		if t == T:
			break

		for i in range(n):
			hit = time_to_wall(i)
			if hit is not None and hit == 0:
				v[i] = -v[i]

	def covered_len(t_abs: Fraction, t0: Fraction, x0, v0) -> Fraction:
		segs = []
		dt = t_abs - t0
		for i in range(n):
			left = x0[i] + Fraction(v0[i]) * dt
			right = left + l[i]
			if right <= 0 or left >= W:
				continue
			if left < 0:
				left = Fraction(0)
			if right > W:
				right = W
			if left < right:
				segs.append((left, right))

		if not segs:
			return Fraction(0)
		segs.sort()

		total = Fraction(0)
		cl, cr = segs[0]
		for nl, nr in segs[1:]:
			if nl > cr:
				total += cr - cl
				cl, cr = nl, nr
			elif nr > cr:
				cr = nr
		total += cr - cl
		return total

	covered_area = Fraction(0)

	for t0, t1, x0, v0 in blocks:
		# Inside one block, each endpoint is linear; union-length changes slope
		# only when two endpoints cross.
		events = {t0, t1}
		ends = []
		for i in range(n):
			slope = Fraction(v0[i])
			c_left = x0[i] - slope * t0
			c_right = c_left + l[i]
			ends.append((c_left, slope))
			ends.append((c_right, slope))

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
			a, b = ts[i], ts[i + 1]
			ca = covered_len(a, t0, x0, v0)
			cb = covered_len(b, t0, x0, v0)
			covered_area += (b - a) * (ca + cb) / 2

	total_area = W * T
	rain_on_road = total_area - covered_area
	ans = rain_on_road * rain_v
	print(f"{float(ans):.2f}")


if __name__ == "__main__":
	main()
