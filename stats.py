def get_num_words(string):
    words = string.split()
    return words

def sort_on(items):
    return items["num"]

def sorted_letters(unsorted):
    sorted_list = []
    for letter in unsorted:
        if letter.isalpha():
            letter_dict = {"char": letter, "num": unsorted[letter]}
            sorted_list.append(letter_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_num_letters(string):
    letter_count = {}
    for letter in string:
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return sorted_letters(letter_count)