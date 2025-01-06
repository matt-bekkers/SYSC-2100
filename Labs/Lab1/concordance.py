"""
SYSC 2100 Winter 2024
Lab 1, Part 3, Exercise 4, Extra-Practice Exercise 5
"""

__author__ = 'Matthé Bekkers'
__student_number__ = '101297066'

import string

# For information about the string module, type help(string) at the shell
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the documentation
# (available @ python.org).


def build_concordance(filename: str) -> dict[str, list[int]]:
    """Return a concordance of words in the text file
    with the specified filename.

    The concordance is stored in a dictionary. The keys are the words in the
    text file. The value associated with each key is a list containing the line
    numbers of all the lines in the file in which the word occurs.)

    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    concordance = {}

    file = open(filename, "r")

    line_count = 0
    for line in file:

        word_list = line.split()
        word_set = set()

        for word in word_list:
            word = word.strip(string.punctuation).lower()
            if word not in word_set and word != "":
                lines_list = concordance.get(word, [])
                lines_list.append(line_count)
                word_set.add(word)
                concordance[word] = lines_list

        line_count += 1


    return concordance



        


# Extra-Practice: Exercise 5 Solution


if __name__ == '__main__':
    pass
    # Write your solution to Extra-practice Exercise 5 here
    filename = 'sons_of_martha.txt'
    print(build_concordance(filename))
