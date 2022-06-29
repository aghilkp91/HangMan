import os
import random
import json

def group_words_by_letter_count():
    # Load a file
    # words taken from /usr/share/dict/words file in unix machine
    file_path = os.path.dirname(os.path.abspath(__file__)) + '/words.txt'
    new_file_path = os.path.dirname(os.path.abspath(__file__)) + '/words_dict.json'
    word_dict_by_letter_count = {}
    with open(file_path) as f:
        # Reading words from file
        words = f.readlines()
        counter = 1
        for word in words:
            word = word.strip()
            word_len = len(word)
            # Add the word into dictionary by number of characters as key
            if word_len in word_dict_by_letter_count:
                word_dict_by_letter_count[word_len].append(word)
                random.shuffle(word_dict_by_letter_count[word_len])
            else:
                word_dict_by_letter_count[word_len] = []
                word_dict_by_letter_count[word_len].append(word)
            print(counter)
            counter += 1
    # Write the result into a json file
    with open(new_file_path, 'w') as outfile:
        json.dump(word_dict_by_letter_count, outfile)



if __name__ == "__main__":
    group_words_by_letter_count()