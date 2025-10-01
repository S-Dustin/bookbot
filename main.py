import sys
from stats import get_num_words, get_num_letters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    FILEPATH = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_text = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    words = get_num_words(book_text)
    print(f"Found {len(words)} total words")

    print("--------- Character Count -------")
    letters = get_num_letters(book_text)
    for letter in letters:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


main()