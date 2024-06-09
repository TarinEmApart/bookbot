def main():
    path_to_file = 'books/frankenstein.txt'
    text = book_text(path_to_file)
    word_count_number = word_count(text)
    char_count = count_characters(text)
    list_of_dicts = convert_dict_to_list_of_dicts(char_count)
    print_report(list_of_dicts, path_to_file, word_count_number)

def book_text(path):
    with open(path) as file:
        file_contents = file.read()

        return file_contents

def word_count(text):
    return len(text.split())

def count_characters(text):
    all_words = text.split()
    alphabet_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for word in all_words:
        word_lower = word.lower()
        list = []
        for letter in word_lower:
            list.append(letter)
        for letter in list:
            for key in alphabet_dict:
                if letter == key:
                    alphabet_dict[key] += 1
    return alphabet_dict

def sort(list_of_dicts):
    return list_of_dicts["num"]

def convert_dict_to_list_of_dicts(char_count):
    list_of_dicts = []
    for pair in char_count:
        key = pair
        value = char_count[pair]
        word_dict = {"letter": key, "num": value}
        list_of_dicts.append(word_dict)
    list_of_dicts.sort(reverse=True, key=sort)
    return list_of_dicts

def print_report(list_of_dicts, path_to_file, word_count_number):
    print(f"--- Begin report of {path_to_file} --- ")
    print("")
    print(f"{word_count_number} words found in the document")
    print("")
    for dict in list_of_dicts:
        letter_value = dict["letter"]
        num_value = dict["num"]
        print(f"The {letter_value} character was found {num_value} times.")
    print("")
    print("--- End report. ---")
main()