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
import numpy # useful for working with tensors
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
    messages = load_data(path=INPUT_FILE_PATH)
    
    # a) How many sentences are there? (ignores empty lines -> see load_data function)
    print(f"Number of Messages (File: {INPUT_FILE_PATH}): {len(messages)}")
# end main


# loads data from the data.txt file
# ignores lines with character length of zero
def load_data(path:str)-> list[str]:
    lines:list[str] = []
    with open(file=path, mode='r') as file:
        for line in file:
            if len(line) > 0:
                lines.append(line)
    return lines
# end load_data


if __name__ == "__main__":
    main()
