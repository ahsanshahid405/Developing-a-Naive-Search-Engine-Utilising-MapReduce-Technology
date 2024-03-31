#!/usr/bin/env python

import sys
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from collections import defaultdict

# Function to remove punctuation
def remove_punctuation(text):
    punctuation_chars = '''!()-[]{};:'"\,<>./|=?@#$%^+&*_~'''
    text_without_punctuation = ''.join(char for char in text if char not in punctuation_chars)
    return text_without_punctuation

# Function to remove extra line
def remove_extra_line(text):
    punctuation_chars = '\n'
    text_without_special_char = ''.join(char for char in text if char not in punctuation_chars)
    return text_without_special_char

# Function to tokenize text
def tokenize_text(text):
    return word_tokenize(text)

# Function to remove stopwords
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word.lower() not in stop_words]

# Function to preprocess data
def preprocess_data(data):
    data = data.lower()
    data = remove_punctuation(data)
    data = remove_extra_line(data)
    data = tokenize_text(data)
    data = remove_stopwords(data)
    return data

if __name__ == "__main__":
    # Vocabulary will be collected in a dictionary with term as key and term_id as value
    vocab = {}
    current_term_id = 0

    # IDF values will be collected in a dictionary with term_id as key and df_t as value
    idf_values = defaultdict(int)

    # Term Frequency (TF) will be collected in a dictionary with article_id as key and dictionary of term_id:count as value
    tf_values = defaultdict(dict)

    # Total number of documents
    total_documents = 0

    for line in sys.stdin:
        try:
            # Read each line from input
            data = line.strip()
            # Assuming data is in CSV format
            columns = data.split(',')
            article_id = columns[0]
            section_text = columns[1]

            # Preprocess section text
            section_text = preprocess_data(section_text)
            
            # Calculate Term Frequency (TF) for the current document
            term_freq = defaultdict(int)
            for term in section_text:
                if term not in vocab:
                    vocab[term] = current_term_id
                    current_term_id += 1
                term_id = vocab[term]
                term_freq[term_id] += 1

            # Update IDF values
            for term_id in set(term_freq.keys()):
                idf_values[term_id] += 1
            
            # Update TF values
            tf_values[article_id] = term_freq

            total_documents += 1

        except Exception as e:
            # Handle exceptions
            pass
    
    # Calculate IDF values
    for term_id, df_t in idf_values.items():
        idf_values[term_id] = total_documents / df_t

    # Emit vocabulary, TF, and IDF values
    for term, term_id in vocab.items():
        print(f"VOCAB\t{term}\t{term_id}")
    for article_id, term_freq in tf_values.items():
        print(f"TF\t{article_id}\t{term_freq}")
    for term_id, idf in idf_values.items():
        print(f"IDF\t{term_id}\t{idf}")
