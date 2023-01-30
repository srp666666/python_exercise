# program to get the number of words
from collections import defaultdict


def create_word_length_dict(sentence):
    word_length_dict = defaultdict(lambda: defaultdict(int))
    lines = sentence.strip().split(".")
    for line_num, line in enumerate(lines):
        for word in line.strip().split():
            word_length = len(word)
            word_length_dict[line_num][word_length] += 1
    return word_length_dict


original_sentence = input('Please enter a sentence')
print(create_word_length_dict(original_sentence))
