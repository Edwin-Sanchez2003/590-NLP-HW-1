"""
    Homework 01
    590 Natural Language Processing
    Edwin Sanchez
    
    Dataset Generator
    Reads the data from a json file,
    extracting only the messages, and writes
    them onto lines in a text file.
"""


# Packages
import json # read json files
import argparse

# description for argparse
descr = """
Reads the data from a json file,
extracting only the messages, and writes
them onto lines in a text file.
"""

# argument parser object
parser = argparse.ArgumentParser(
                    prog='Dataset Generator',
                    description=descr)

# path to file to be extracted
parser.add_argument('-i', '--input_file_path', help="The path to the file you want to extract data from. Must be in JSON file format.")
parser.add_argument('-o', '--output_file_path', help="The path to the file you want to write the extracted data to. Assumes txt file.")

# parse args
args = parser.parse_args()
INPUT_FILE_PATH = str(args.input_file_path)
OUTPUT_FILE_PATH = str(args.output_file_path)


def main():
    # load the json file
    data = load_json_file(path=INPUT_FILE_PATH)
    
    # extract message data
    message_data = extract_data(data=data)
    
    # write back to a text file
    write_to_txt(path=OUTPUT_FILE_PATH, lines=message_data)
# end main


# extracts message data from a json file
# returns a list of strings, each string 
# being a message.
def extract_data(data:list[dict])->list[str]:
    messages:list[str] = []
    for sample in data:
        for msg in sample["messages"]:
            messages.append(msg)
    return messages
# end extract_data


# write a list of strings to a text file
def write_to_txt(path:str, lines:list[str])->None:
    with open(file=path, mode='w') as file:
        for line in lines:
            file.write(line + '\n')
# end write_to_txt


# takes a path to a json file and loads it into a python dictionary
def load_json_file(path:str)->list[dict]:
    lines:list[dict] = []
    with open(file=path, mode="r") as file:
        samples = list(file)
        for line in samples:
            lines.append(json.loads(line))
    return lines
# end load_json_file


if __name__ == "__main__":
    main()
    