#!/usr/bin/python
import nltk
from nltk import pos_tag
from nltk.corpus import brown
from nltk import word_tokenize, sent_tokenize
from collections import defaultdict

#--- xml ---
from xml.etree import ElementTree as ET


# Function: print_error
# ---------------------
# notifies the user of an error, how to correct it, then exits
def print_error (error_message, correction_message):
	print "ERROR: 	", error_message
	print "	---"
	print "	", correction_message
	exit ()



# Function: get_descriptor_counts
# ----------------------------------
# given the corpus, this function will associate each adjective to a count
# for the number of times it modifies the query word.
def get_descriptor_counts (query_word, corpus):

	descriptor_counts = defaultdict(lambda: 0)

	for sentence in corpus:
		words = [element[0].lower() for element in sentence]
		tags = [element[1] for element in sentence]

		if query_word in words:
			index = words.index(query_word);



def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)



# Function: get_all_dependencies
# -------------------------------
# return all dependencies 
def get_all_dependencies (xml_doc_name):

	tree = ET.parse (xml_doc_name);
	root = tree.getroot ();

	dependencies = []
	for dep in root.findall('.//dep'):
		governor = dep.find('governor')
		dependent = dep.find ('dependent')
		dependencies.append ((dep.attrib['type'], governor.text, dependent.text))

	return dependencies



# Function: get_adj_vectors
# ------------------------
# given a list of all dependencies, this will assemble
# all 'adj_vector', which is a defaultdict(lambda: 0) that maps adjectives
# to the number of times they modify the word
def get_adj_vectors (query_word, all_dependencies):


	adj_vectors = defaultdict (lambda: None)

	### Step 1: get raw counts ###
	for dep in all_dependencies:
		dep_type = dep[0]
		governor = dep[1]
		dependent = dep[2]

		if dep_type == 'amod' or dep_type == 'appos' or dep_type == 'num':
			if not adj_vectors[governor]:
				adj_vectors[governor] = defaultdict (lambda: 0.0)
			adj_vectors[governor][dependent] += 1


	### Step 2: normalize ###
	for word in adj_vectors.keys ():

		#--- get the total # of adjectives that have modified it ---
		total = 0.0
		for adjective in adj_vectors[word].keys():
			total += adj_vectors[word][adjective]

		#--- divide each entry appropriately ---
		for adjective in adj_vectors[word].keys():
			adj_vectors[word][adjective] = float(adj_vectors[word][adjective]) / total

	return adj_vectors


# Function: get_top_euphamism_candidates
# ----------------------------------
# this function will return a list of (word, similarity) tuples
def get_top_euphamism_candidates (query_word, corpus):

	descriptor_counts =	get_descriptor_counts (query_word, corpus);







if __name__ == "__main__":

	#--- corpus name
	corpus_file = 'brown_corpus_sample.txt.xml'
	query_word = 'funds'

	#--- get all dependencies
	all_dependencies = get_all_dependencies (corpus_file)

	#--- get adj_vector for this word
	adj_vectors = get_adj_vectors (query_word, all_dependencies)

	print adj_vectors['jury']








