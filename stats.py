def get_num_words(string):
    words = string.split()
    print(f"Found {len(words)} total words")

def get_num_letters(string):
    letter_count = {}
    for letter in string:
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    print(letter_count)