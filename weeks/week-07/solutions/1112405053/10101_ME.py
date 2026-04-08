import sys


# 7-segment bitmask for digits 0..9 (a,b,c,d,e,f,g).
SEG = [
	0x3F,  # 0
	0x06,  # 1
	0x5B,  # 2
	0x4F,  # 3
	0x66,  # 4
	0x6D,  # 5
	0x7D,  # 6
	0x07,  # 7
	0x7F,  # 8
	0x6F,  # 9
]


def build_transitions() -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
	remove_to = [[] for _ in range(10)]
	add_to = [[] for _ in range(10)]
	move_within = [[] for _ in range(10)]
 
	for d in range(10):
		for nd in range(10):
			if d == nd:
				continue
			x = SEG[d] ^ SEG[nd]
			c_d = SEG[d].bit_count()
			c_nd = SEG[nd].bit_count()

			# Move one stick inside one digit: remove one segment and add one segment.
			if c_d == c_nd and x.bit_count() == 2:
				move_within[d].append(nd)

			# Remove one stick from this digit.
			if c_d == c_nd + 1 and x.bit_count() == 1:
				remove_to[d].append(nd)

			# Add one stick to this digit.
			if c_d + 1 == c_nd and x.bit_count() == 1:
				add_to[d].append(nd)

	return remove_to, add_to, move_within


def parse_side(
	s: str,
	offset: int,
	side_factor: int,
	coeff: dict[int, int],
	digit_positions: list[int],
) -> None:
	i = 0
	n = len(s)
	sign = 1

	if i < n and s[i] == "-":
		sign = -1
		i += 1

	while i < n:
		j = i
		while j < n and s[j].isdigit():
			j += 1

		# Digits s[i:j] are one number token.
		for k in range(i, j):
			place = j - 1 - k
			idx = offset + k
			coeff[idx] = side_factor * sign * (10 ** place)
			digit_positions.append(idx)

		if j >= n:
			break

		sign = 1 if s[j] == "+" else -1
		i = j + 1


def solve(expr_with_hash: str) -> str:
	expr = expr_with_hash
	p = expr.find("#")
	if p == -1:
		core = expr
	else:
		core = expr[:p]

	eq = core.find("=")
	left = core[:eq]
	right = core[eq + 1 :]

	coeff: dict[int, int] = {}
	digit_positions: list[int] = []
	parse_side(left, 0, 1, coeff, digit_positions)
	parse_side(right, eq + 1, -1, coeff, digit_positions)

	chars = list(core)
	digits = {idx: ord(chars[idx]) - ord("0") for idx in digit_positions}

	base_f = 0
	for idx in digit_positions:
		base_f += coeff[idx] * digits[idx]

	remove_to, add_to, move_within = build_transitions()

	for i in digit_positions:
		d = digits[i]
		c = coeff[i]
		for nd in move_within[d]:
			if base_f + c * (nd - d) == 0:
				out = chars[:]
				out[i] = str(nd)
				return "".join(out) + "#"

	for i in digit_positions:
		d1 = digits[i]
		c1 = coeff[i]
		for nd1 in remove_to[d1]:
			delta1 = c1 * (nd1 - d1)
			need = -base_f - delta1

			for j in digit_positions:
				if j == i:
					continue
				d2 = digits[j]
				c2 = coeff[j]
				for nd2 in add_to[d2]:
					if c2 * (nd2 - d2) == need:
						out = chars[:]
						out[i] = str(nd1)
						out[j] = str(nd2)
						return "".join(out) + "#"

	return "No"


def main() -> None:
	raw = sys.stdin.buffer.read().decode(errors="ignore")
	if not raw:
		return
	sys.stdout.write(solve(raw.strip()))


if __name__ == "__main__":
	main()
