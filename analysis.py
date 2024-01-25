"""
    Homework 01
    590 Natural Language Processing
    Edwin Sanchez
    
    Analysis
    This file contains the code used
    to determine the answers to questions
    for Problem 5 of Homework 01.
"""


# Packages
import nltk # string parsing library
from nltk.probability import FreqDist
import argparse # parse arguments passed to the file

# description for argparse
descr = """
This file contains the code used
to determine the answers to questions
for Problem 5 of Homework 01.
"""

# argument parser object
parser = argparse.ArgumentParser(
                    prog='Analysis',
                    description=descr)

# path to file to be extracted
parser.add_argument('-i', '--input_file_path', help="The path to the file you want to read message data from.")

# parse args
args = parser.parse_args()
INPUT_FILE_PATH = str(args.input_file_path)


def main():
    # load the data
    text = load_data(path=INPUT_FILE_PATH)
    print(f"File: {INPUT_FILE_PATH}")
    
    # get sentence tokens from the text
    sentences = nltk.sent_tokenize(text=text, language="english")
    
    # a) How many sentences are there? (ignores empty lines)
    print(f"Number of Sentences: {len(sentences)}")
    
    # split sentences by words using spaces
    num_tokens = 0
    for sentence in sentences:
        sentence:str
        num_tokens += len(sentence.split(' '))
    # end for
    
    # b) How many tokens are there?
    print(f"Number of Tokens: {num_tokens}")
    
    # split using nltk's word_tokenize() function
    num_tokens_nltk = nltk.word_tokenize(text=text, language="english")
    
    # c) How many tokens are there now?
    print(f"Number of Tokens: {len(num_tokens_nltk)}")

    # lowercase all of the words
    lower_case_text = text.lower()
    tokens_nltk_lower = nltk.word_tokenize(text=lower_case_text, language="english")
    freq_dist = FreqDist(tokens_nltk_lower)
    print(freq_dist.most_common(n=10))
    
    # d) how many tokens and types are there now?
    print(f"Number of Tokens: {len(tokens_nltk_lower)}")
    print(f"Number of Types: {len(freq_dist)}")
    
    # e)
    
    
    # f) what is the most frequent word type?
    print(f"Most Frequent Word Type: {freq_dist.most_common(n=1)}")
    
    # f) what is the 5th most frequent word type?
    print(f"5th Most Frequent Word Type: {freq_dist.most_common(n=5)[-1]}")
# end main


def exists(types_list:list, possible_type:str)->bool:
    for type_val in types_list:
        if type_val == possible_type:
            return True
    return False
# end exists


# loads data from the data.txt file
def load_data(path:str)-> str:
    text = ""
    with open(file=path, mode='r') as file:
        for line in file:
            text += line
    return text
# end load_data


if __name__ == "__main__":
    main()
