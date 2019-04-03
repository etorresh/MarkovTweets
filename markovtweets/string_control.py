# Removes unnecessary blank spaces. (Blank space next to blank space, blank space behind periods)
def clean_blank_space(string_input):
    base = 0
    clean_list = []
    for _ in string_input:
        # Prevents index out of range.
        if base == len(string_input) - 1:
            clean_list.append(string_input[base])
            break
        elif string_input[base] == " " and string_input[base + 1] == ".":
            pass
        elif string_input[base] == " " and string_input[base + 1] == " ":
            pass
        else:
            clean_list.append(string_input[base])
        base += 1
    return "".join(clean_list)


# Removes alpha characters from the end of a string that are not a period or question mark.
def remove_non_alpha(string_input):
    clean_list = string_input.split()
    for _ in clean_list:
        if clean_list[-1].isalpha() is False and clean_list[-1] != "." and clean_list[-1] != "?":
            del clean_list[-1]
    return " ".join(clean_list)


# Removes last words from string until the character limit is reached. Adds priority message at the end of the string.
def limit_check(string_input, char_limit, extra_message =""):
    if len(string_input) > char_limit:
        string_input = string_input.split()
        while True:
            del string_input[-1]
            if len("".join(string_input)) <= char_limit - 1 - len(extra_message):
                break
    return "".join(string_input) + " " + extra_message
