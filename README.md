590 Natural Language Processing | Edwin Sanchez
# Homework 1 - Problem 5
The code in this repo is used to complete Problem 5 of Homework 1 for 590 Natural Language Processing.

## Environment Setup

* **Python Version:** 3.11.5 *(should work with python versions 3.11.X. Type Hints may lead to compatibility issues with older python versions)*
* **OS Used:** Windows Subsystem for Linux, Version 2 (WSL2) on Windows 11

1. Create a python environment: `conda create -n hw-1 python=3.11.5`
2. Activate the environment: `conda activate hw-1`
3. Install the required packages: `pip install -r requirements.txt`

## data_generator.py

## analysis.py



## Useful Commands
* **Extract Messages From Original Data:** `python data_generator.py -i ./original_data/train.jsonl -o ./data.txt`
* **Perform Text Analysis On Message Data:** `python analysis.py -i ./data.txt`

## Citations
nocite: "[@*]"
references:
- author:
  - family: Peskov
    given: Denis
  - family: Cheng
    given: Benny
  - family: Elgohary
    given: Ahmed
  - family: Barrow
    given: Joe
  - family: Danescu-Niculescu-Mizil
    given: Cristian
  - family: Boyd-Graber
    given: Jordan
  container-title: Association for computational linguistics
  id: "Peskov:Cheng:Elgohary:Barrow:Danescu-Niculescu-Mizil:Boyd-Graber-2020"
  issued: 2020
  publisher-place: Seattle
  title: "It takes two to lie: One to lie and one to listen"
  title-short: It takes two to lie
  type: paper-conference
---