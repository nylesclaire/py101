# further exploration

# determine if line is too long (> max_width)
# find index of the end of the last word, before index max_width - 1
# split string at that index, into two strings.
# test second string produced by the split for its width, repeat process.
# with each of the newly produced shorter strings, compare and determine the longest length
# set padding width based on max length
# create box w/ each string on its own line.

def print_in_box2(line, max_width=(float('inf'))):
    max_line = max_width - 4
    list_of_lines = []
    while len(line) > max_line:
        index = max_line
        while index > 0:
            if line[index] == " ":
                end_of_word_idx = index
                break
            index -= 1
        list_of_lines.append(line[:end_of_word_idx])
        line = line.removeprefix(line[:end_of_word_idx])
        line = line.strip()
    list_of_lines.append(line)

    line_lengths_list = []
    for item in list_of_lines:
        line_lengths_list.append(len(item))
    len_longest_line = max(line_lengths_list)

    padded_width = len_longest_line + 2
    horizontal_rule = f"+{"-" * padded_width}+"
    empty_line = f"|{" " * padded_width}|"

    print(horizontal_rule)
    print(empty_line)
    for item in list_of_lines:
        print(f"|{item.center(padded_width)}|")
    print(empty_line)
    print(horizontal_rule)


# print_in_box2('To boldly go where no one has gone before.')
print_in_box2(
   f"And that little me, I could hardly recognize her. You know, she was so carefree and, like, fearless. She just loved every part of herself.", 60)