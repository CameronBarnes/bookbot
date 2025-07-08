from typing import Any

def num_words(text: str) -> int:
	return len(text.split())

def count_chars(text: str) -> dict[str, int]:
	out = {}
	for char in text.lower():
		if char not in out:
			out[char] = 0
		out[char] += 1
	return out

def sort_on(items):
	return items["num"]

def format_chars(chars: dict[str, int]) -> list[dict[str, Any]]:
	out: list[dict[str, Any]] = []
	for char in chars:
		out.append({"char": char, "num": chars[char]})
	out.sort(reverse=True, key=sort_on)
	return out
