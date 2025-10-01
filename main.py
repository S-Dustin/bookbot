from stats import get_num_words, get_num_letters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    get_num_words(book_text)
    get_num_letters(book_text)


main()