# expected input: a short string
# expected output: None; print a multi-line strings w/ dashes, etc.

# determine length of the string
# print a version w/ padding on either side and 
# the | character on either side of that
# print a multiline version w/ two empty lines top and bottom framed by |
# add more lines to the multiline version w/ dashes for top and bottom


def print_in_box(line):
    padded_width = len(line) + 2
    print_this = (
        f"+{"-" * padded_width}+\n"
        f"|{" " * padded_width}|\n"
        f"|{line.center(padded_width)}|\n"
        f"|{" " * padded_width}|\n"
        f"+{"-" * padded_width}+\n"
    )
    print(print_this)

#examples
print_in_box('To boldly go where no one has gone before.')
print_in_box('')