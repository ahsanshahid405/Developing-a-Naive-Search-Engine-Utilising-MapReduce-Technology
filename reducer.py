#!/usr/bin/env python

import sys
from collections import defaultdict

# Function to convert TF-IDF weights into vectors
def weights_to_vector(weights, vocabulary_size):
    vector = [0] * vocabulary_size
    for word_id, weight in weights.items():
        vector[word_id] = weight
    return vector

if __name__ == "__main__":
    # Vocabulary will be collected in a dictionary with term as key and term_id as value
    vocab = {}

    # IDF values will be collected in a dictionary with term_id as key and idf as value
    idf_values = {}

    # TF values will be collected in a dictionary with article_id as key and dictionary of term_id:count as value
    tf_values = defaultdict(dict)

    for line in sys.stdin:
        try:
            # Read each line from input
            line_type, *data = line.strip().split('\t')

            if line_type == 'VOCAB':
                term, term_id = data
                vocab[term_id] = term
            elif line_type == 'TF':
                article_id, term_freq = data
                term_freq = dict(map(int, pair.split(':')) for pair in term_freq.split())
                tf_values[article_id] = term_freq
            elif line_type == 'IDF':
                term_id, idf = data
                idf_values[term_id] = idf
        
        except Exception as e:
            # Handle exceptions
            pass
    
    # Calculate TF-IDF weights and emit document vectors
    for article_id, term_freq in tf_values.items():
        tfidf_weights = {}
        for term_id, tf in term_freq.items():
            idf = idf_values[term_id]
            tfidf_weights[term_id] = tf * idf
        vector = weights_to_vector(tfidf_weights, len(vocab))
        print(f"{article_id}\t{' '.join(map(str, vector))}")
