# String manipulation for AMLO Simulator.
# Made by MadreNodriza. https://github.com/MadreNodriza

import random


# Removes extra spaces from a string.
def less_spaces(string_input):
    base = 0
    clean_list = []
    for x in string_input:
        # Prevents index out of range.
        if base == len(string_input) - 1:
            clean_list.append(string_input[base])
            break
        if string_input[base] == " " and string_input[base + 1] == " ":
            pass
        else:
            clean_list.append(string_input[base])
        base += 1
    return "".join(clean_list)


# Removes any space that's is behind a period.
def clean_periods(string_input):
    base = 0
    clean_list = []
    for x in string_input:
        # Prevents index out of range.
        if base == len(string_input) - 1:
            clean_list.append(string_input[base])
            break
        if string_input[base] == " " and string_input[base + 1] == ".":
            pass
        else:
            clean_list.append(string_input[base])
        base += 1
    return "".join(clean_list)


def super_detox(string_input):
    return clean_periods(less_spaces(string_input))


# Removes non alpha characters that are at the end of a character except question marks.
def remove_non_alpha_endings(input):
    clean_list = []
    for x in input:
        clean_list.append(x)
    for y in clean_list:
        if clean_list[-1].isalpha() == False and clean_list[-1] != "?":
            del clean_list[-1]
    return"".join(clean_list)


# Removes alpha characters from the end of a string that are not a period or question mark.
def only_periods(string_input):
    clean_list = []
    for x in string_input:
        clean_list.append(x)
    for y in clean_list:
        if clean_list[-1].isalpha() == False and clean_list[-1] != ".":
            del clean_list[-1]
    return "".join(clean_list)


# Adds random words from a list at the end of a string.
def add_random_words(string_input, word_list):
    return string_input + random.choice(word_list)


# Removes last words from string until the character limit is reached. Can add extra_message at the end.
def limit_check(string_input, char_limit, extra_message =""):
    if len(string_input) > char_limit:
        string_input = string_input.split()
        while True:
            del string_input[-1]
            if len("".join(string_input)) <= char_limit - 1 - len(extra_message):
                break
    return "".join(string_input) + " " + extra_message
