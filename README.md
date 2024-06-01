## Developing-a-Naive-Search-Engine-Utilising-MapReduce-Technology
**Dependencies:**
* Jupyter Notebook ([install](https://docs.jupyter.org/en/latest/install.html))
* IPython ([install](https://ipython.org/install.html))
* Pandas ([install](https://pandas.pydata.org/docs/getting_started/install.html))
* NumPy ([install](https://numpy.org/install/))
* Nltk  ([install](https://www.nltk.org/install.html))

* **Introduction:**
This repository contains implementation of Developing a Naive Seearch Engine Utilising Mapreduce Technology, which leverages a dataset of Wikipedia CSV file containing 5 million rows, utilising a Map-Reduce Technology as part of an assignment for the Fundamental of Big Data Analytics (DS2004) course.

* **Where Our Solution Differs:**
In the MapReduce paradigm, Hadoop plays a critical role in distributing and managing the processing of vast datasets across a cluster of interconnected computers. It facilitates job scheduling and management, ensuring that Map and Reduce tasks are executed efficiently across the cluster's nodes. Hadoop handles the distribution of input data blocks, striving to minimize data movement across the network by processing data locally whenever feasible. Moreover, it offers fault tolerance mechanisms, automatically replicating data blocks and restarting failed tasks to maintain job integrity and reliability. Hadoop's resource management capabilities dynamically allocate computational resources to tasks, optimizing cluster utilization and performance. Overall, Hadoop serves as the underlying framework that enables the scalable and parallel processing of data in the MapReduce model, making it feasible to tackle large-scale data analysis tasks efficiently.

* **Vector Space Model for Information Retrieval:**
To understand the vector space model better, we have done several steps
 1) Term:
 	we have made a term that refers to a distinct word.
 2) Vocabulary:
 	We made  a vocabulary consisting of all the unique terms found in the corpus.
 3) Term Frequency :
	in Term Frequency (TF) we have represented how often a term t appears in a document d.
	The documents mentioned earlier can be depicted using Term Frequency (TF), where
	each term is formatted as (ID, frequency).

* **Inverse Document Frequency (IDF):**
Inverse Document Frequency (IDF) indicates the number of documents in which
a term appears, reflecting its commonality. A high Inverse Document Frequency (IDF)
suggests that the term is not particularly distinctive across documents.

* **TF/IDF Weights:**
TF/IDF weights are essentially term frequencies adjusted by Inverse Document
Frequency (IDF) normalization. In this step, we have observed the terms with IDs and reduced them in scale.

* **Basic Vector Space Model:**
In the basic vector space model, documents and queries are represented as
vectors, reflecting their TF/IDF weights.
we have followed the these steps:
    * Iterate through term frequencies in each document.
    * Calculate TF by dividing term frequency by total words in the document.
    * Retrieve IDF from the idf_values dictionary.
    * Compute TF-IDF as the product of TF and IDF.
    * Store TF-IDF weights for each term under the corresponding document ID in tfidf_weights dictionary.
* **Query:**
* Preprocessing: 
  The preprocessing_data function takes a text input and applies several preprocessing steps, including converting text to lowercase, removing manual punctuation, eliminating extra line 
  breaks, tokenizing the text, and removing stopwords.
* Matching Vocabulary: 
  After preprocessing the query, the code initializes a list query_matching_vocab with zeros, indicating the absence of terms in the query within the vocabulary. It then iterates through the 
  preprocessed query terms and checks if each term exists in the vocabulary. If a term is found, it sets the corresponding index in query_matching_vocab to 1.
* Matching Indices: 
  The code then identifies the indices where the query terms match with the vocabulary and stores them in the matching_indices list.
* Mapping Vocabulary IDs:
  It creates a dictionary query_id to map the vocabulary terms to their respective indices for further processing.
  Term Frequency (TF) Calculation: It calculates the term frequency (TF) of each query term within the documents.
  Inverse Document Frequency (IDF) Calculation: It computes IDF values for the query terms based on their occurrence within the corpus.
  TF/IDF Weight Calculation: 
  Using TF and IDF values, the code calculates TF/IDF weights for each term in each document. It iterates through the documents, computes TF/IDF weights for each term, and stores them in the 
  query_tfidf_weights dictionary.
    
    
* **Microsoft Azure** 
For Apache Hadoop cluster we have used Microsoft Azure. We created one master and two slaves. After uploading our mapper, reducer and data set files on Virtual machines in Azure we encountered some errors while trying to run those files. Firstly our files were stored in /home/hadoop-master folder and when we tried to run our map-reduce files we encountered permission denied error. Then we moved all our files from hadoop-master folder to hadoopuser folder and tried running them again but still encountered the same error. And then encountered the same error again when we moved our files from hadoop-user to home. Firstly we wrote our whole code in a single when and it was working fine and was giving correct output. Then we converted it into mapper and reducer files but encountered permission-denied errors while running the mapper file on master. We did a lot of research to resolve the error but could not find the solution.

* **Contributors:**
Ahsan Abdul  (i221870@nu.edu.pk)
Awais Arshad (i221989@nu.edu.pk)
Ali Zaib     (i221900@nu.edu.pk)

