import os
import re

text_files = [f for f in os.listdir() if f[-3:] == 'txt']


def separate_lines(lines: list) -> list:
    """
    Function which removes all empty lines from list received from reading text file
    :param lines:
    :return:
    """
    return [line for line in lines if line != "\n"]


def remove_special_characters(file_string):
    filtered_text = re.sub('[,./;\n]', " ", file_string)
    return filtered_text


def count_occurrences(word_list: list, searched_word: str):
    word_count = 0
    for line in word_list:
        for word in line.split(' '):
            if word.lower() == searched_word.lower():
                word_count += 1
    return word_count


while True:
    print(f"Please select file to count specific words in, out of: ")
    for index, el in enumerate(text_files):
        print(F"{index + 1}: {el}")
    text_file_input = int(input())

    try:
        with open(text_files[text_file_input - 1], 'r') as text_file:
            all_lines = separate_lines(text_file.readlines())
            words_list = list(map(remove_special_characters, all_lines))
            if not all_lines:
                print("File contains no words, please select different one")
            else:
                break
    except FileNotFoundError:
        print("File not found, did you make a typo?")
    except IndexError:
        print("Please select one of available files.")

count_input = input("Which word would you like to make a count for? ")
#
print(f"There are {count_occurrences(words_list, count_input)} occurencies of a word '{count_input}' in selected file.")
