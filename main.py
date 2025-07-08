
def get_book_text(path: str):
	with open(path) as file:
		return file.read()

def main():
	from stats import format_chars, num_words, count_chars
	import sys
	if len(sys.argv) == 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path = sys.argv[1]
	text = get_book_text(path)
	num = num_words(text)
	chars = count_chars(text)
	chars = format_chars(chars)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {num} total words")
	print("--------- Character Count -------")
	for char in chars:
		c = char["char"]
		num = char["num"]
		print(f"{c}: {num}")
	print("============= END ===============")


main()
