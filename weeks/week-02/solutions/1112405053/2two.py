import sys


def shift_letters(text: str, shift: int = 4) -> str:
	"""Shift all English letters by 4 positions (Caesar cipher).
	Z shifts to D, a shifts to e, etc. Non-letter characters remain unchanged."""
	result = []
	for char in text:
		if 'A' <= char <= 'Z':
			# Uppercase letters
			new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
			result.append(new_char)
		elif 'a' <= char <= 'z':
			# Lowercase letters
			new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
			result.append(new_char)
		else:
			# Non-letter characters remain unchanged
			result.append(char)
	return ''.join(result)


def main():
	data = sys.stdin.read()
	if not data:
		return
	result = shift_letters(data.rstrip('\n'))
	print(result)


if __name__ == '__main__':
	main()
