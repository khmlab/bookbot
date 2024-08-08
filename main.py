def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_chars(text)
    chars_sorted_list = chars_dict_to_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_chars(text):
    char_count = {}
    for char in text:
        lowered = char.lower()
        if lowered.isalpha():
            if lowered in char_count.keys():
                char_count[lowered] += 1
            else:
                char_count[lowered] = 1
        else:
            pass
    return char_count


def chars_dict_to_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(chars_dict):
    return chars_dict["num"]


if __name__ == "__main__":
    main()
