import os

files2 = [f for f in os.listdir() if f[-3:] == 'txt']
def separate_lines(lines):
    return [line for line in lines if line != "\n"]

def filter_file(file_string: str) -> list:
    bad_chars = [',', '.', ';', '\n', '!']
    for i in bad_chars:
        if i in file_string:
            file_string = file_string.replace(i, '')
    return file_string.split(" ")


def count_occurencies(word_list: list, searched_word: str):
    word_count = 0
    for word in word_list:
        if word.lower() == searched_word.lower():
            word_count += 1
    return word_count


while True:
    text_file_input = input(f"Please select file to count specific words in, out of: {', '.join(files2)} ")
    try:
        with open(text_file_input, 'r') as text_file:
            all_lines = separate_lines(text_file.readlines())
            if not all_lines:
                print("File contains no words, please select different one")
            else:
                break
    except FileNotFoundError:
        print("File not found, did you make a typo?")

# words_list = filter_file(all_text)
#
# count_input = input("Which word would you like to make a count for? ")
#
# print(f"There are {count_occurencies(words_list, count_input)} occurencies of a word '{count_input}' in selected file.")
