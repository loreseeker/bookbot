import string

def count_words(word_string):
    frills = word_string.split()
    return len(frills)

def count_characters(word_string):
    char_dict = {}
    for elem in word_string:
        celem = elem.lower()
        if celem not in char_dict:
            char_dict[celem] = 1
        else:
            char_dict[celem] += 1
    return char_dict

def main():
    print("Report:")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("Word count:", count_words(file_contents))
        char_dict = count_characters(file_contents)
        for key in string.ascii_lowercase:
            print(key, ":", char_dict[key])


main()

