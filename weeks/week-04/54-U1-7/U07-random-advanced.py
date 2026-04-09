import random
import secrets

def main() -> None:
	random.seed(42)
	seq1 = [random.randint(1, 100) for _ in range(5)]
	random.seed(42)
	seq2 = [random.randint(1, 100) for _ in range(5)]
	print(seq1 == seq2)

	rng1 = random.Random(1)
	rng2 = random.Random(2)
	print(rng1.random(), rng2.random())

	print(secrets.randbelow(100))
	print(secrets.token_hex(16))
	print(secrets.token_bytes(16))


if __name__ == "__main__":
	main()
