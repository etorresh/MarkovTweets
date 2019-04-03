# -*- coding: utf-8 -*-

import random

from . import string_control


def read_file(filename):
    with open(filename, "r", encoding = "utf-8") as file:
        content = file.read().replace("\n", " ")
    return content


def build_chain(source, chain={}):
    words = source.split(" ")
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    return chain


# Remove spaces from last word.
# Add starting sentence to markov chain.
def create_message(chain, max_length=40, starting_sentence=""):
    if starting_sentence != "":
        starting_sentence = string_control.clean_blank_space(starting_sentence)
        starting_sentence = starting_sentence.strip()
        if starting_sentence[-1] == "?":
            starting_sentence = starting_sentence + random.choice([" Si,", " No,"])

        word1 = starting_sentence.split(" ")[-1]
        message = starting_sentence
        if word1 not in chain:
            word1 = random.choice(list(chain.keys()))
    else:
        word1 = random.choice(list(chain.keys()))
        message = word1.capitalize()

    while len(message.split(" ")) < max_length:
        # Check if word limit is reached and if it's true end while loop.
        if word1 not in chain:
            return message

        word2 = random.choice(chain[word1])
        word1 = word2
        message += " " + word2
        last_word = message[len(message) - 1]

    message = string_control.remove_non_alpha(message)

    if str.isalpha(last_word) == False and last_word.isdigit == False:
        message = message[:-1] + "."
    elif last_word != ".":
        message = message + "."
    return message
