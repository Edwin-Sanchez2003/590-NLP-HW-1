590 Natural Language Processing | Edwin Sanchez
# Homework 1 - Problem 5
The code in this repo is used to complete Problem 5 of Homework 1 for 590 Natural Language Processing.

## Environment Setup

* **Python Version:** 3.11.5 *(should work with python versions 3.11.X. Type Hints may lead to compatibility issues with older python versions)*
* **OS Used:** Windows Subsystem for Linux, Version 2 (WSL2) on Windows 11

1. Clone the repository: `git clone https://github.com/Edwin-Sanchez2003/590-NLP-HW-1.git`
2. Create a python environment: `conda create -n hw-1 python=3.11.5`
3. Activate the environment: `conda activate hw-1`
4. Install the required packages: `pip install -r requirements.txt`

That's it! You can run the commands below as needed. You can run the python file with the `-h` argument to get helpful tips on how to run the code.

## Useful Commands
* **Extract Messages From Original Data:** `python data_generator.py -i ./original_data/train.jsonl -o ./data.txt`
* **Perform Text Analysis On Message Data:** `python analysis.py -i ./data.txt -w 1000`


## Packages
* **Natural Language Toolkit (NLTK):** https://www.nltk.org/install.html

## Citations
[1](https://sites.google.com/view/qanta/projects/diplomacy) 
Denis Peskov, undefined., et al, "It Takes Two to Lie: One to Lie and One to Listen," in Association for Computational Linguistics, 2020.
