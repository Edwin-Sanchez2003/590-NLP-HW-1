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
from nltk.probability import FreqDist # freq distribution of the words in the text
import argparse # parse arguments passed to the file
import matplotlib.pyplot as plt # for plotting values
import matplotlib.style as mplstyle
mplstyle.use('fast') # for simplifying plots for large datasets
import pandas as pd

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
parser.add_argument('-w', '--words_to_display', default=0, help="The number of word frequencies (ie. the first 1000 word frequencies) to be plotted on the graph. If 0, no limit will be set.")

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
    print(f"Number of Tokens (split function): {num_tokens}")
    
    # split using nltk's word_tokenize() function
    num_tokens_nltk = nltk.word_tokenize(text=text, language="english")
    
    # c) How many tokens are there now?
    print(f"Number of Tokens (word_tokenize() function): {len(num_tokens_nltk)}")

    # lowercase all of the words
    lower_case_text = text.lower()
    tokens_nltk_lower = nltk.word_tokenize(text=lower_case_text, language="english")
    freq_dist = FreqDist(tokens_nltk_lower)
    #print(freq_dist.most_common(n=10))
    
    # d) how many tokens and types are there now?
    print(f"Number of Token (lowercase): {len(tokens_nltk_lower)}")
    print(f"Number of Types (lowercase): {len(freq_dist)}")
    
    # e) Compare the number of tokens from (b), (c), and (d). Why are they different?
    
    # f) what is the most frequent word type?
    print(f"Most Frequent Word Type: {freq_dist.most_common(n=1)[0]}")
    
    # g) what is the 5th most frequent word type?
    print(f"5th Most Frequent Word Type: {freq_dist.most_common(n=5)[-1]}")
    
    # h) Using the sorted dictionary, draw a graph to see if this data shows the
    #    Zipf's law. X-axis: ranked words, Y-axis: frequencies. Submit your graph
    #    and discuss it (in your pdf). Submit your code as well.

    # re-organize the data to be lists of names & lists of values
    data = freq_dist.most_common()
    norm_freqs:list[float] = []
    num_words = len(data)
    
    norm_freqs:list[float] = []
    for word, _ in data:
        norm_freqs.append(freq_dist.freq(sample=word))
    
    # generate zipfs law values using proportions
    zipf_freq:list[float] = []
    for i in range(len(norm_freqs)):
        zipf_freq.append(1/(i+25))
        
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    num_freqs = 0
    if int(args.words_to_display) == 0:
        num_freqs = num_words
    else:
        num_freqs = int(args.words_to_display)

    plot_data = {
        "data": norm_freqs[:num_freqs],
        "zipf": zipf_freq[:num_freqs]
    } # end plot_data
    
    df = pd.DataFrame(plot_data)
    fig, ax = plt.subplots()

    df['data'].plot(kind='bar', color='red')
    df['data'].plot(kind='line', color='blue')
    df['zipf'].plot(kind="line", color="black")
    plt.legend(["Line-Data", "Line-Zipfs", "Bar-Data"])
    plt.title(f"Word Frequency - Zipf's Law: First {num_freqs} Words")
    plt.xlabel("Words - From highest frequency (left) to lowest (right))")
    plt.ylabel("Word Frequency (Normalized)")
    plt.gca().set_xticklabels([])

    plt.savefig(f"./figures/Zipfs-Bar-Line-Plot:{num_freqs}-Words.png", dpi=300)
    plt.show()
# end main


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
