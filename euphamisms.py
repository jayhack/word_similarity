#!/usr/bin/python

#--- nltk ---
from nltk import pos_tag
from nltk.corpus import brown
from nltk import word_tokenize, sent_tokenize

#--- xml ---
from xml.etree import ElementTree as ET

#--- os/sys ---
import os
import sys

#--- misc ---
import optparse
from collections import defaultdict
import pickle


input_directory = "./data/input"
output_directory = "./data/output"


# Function: print_error
# ---------------------
# notifies the user of an error, how to correct it, then exits
def print_error (error_message, correction_message):
	print "ERROR: 	", error_message
	print "	---"
	print "	", correction_message
	exit ()


class Euphamism_finder:

	#--- Globals ---
	adj_vectors = defaultdict(lambda: None)
	input_directory = None
	output_directory = None



	# Function: load_data
	# --------------------------
	# function to grab all the saved data
	def load_data (self):
		adj_vectors_filename = os.path.join(input_directory, 'adj_vector.obj')
		print "---> Loading: " + adj_vectors_filename
		input = open (adj_vectors_filename, 'rb')
		adj_vectors = pickle.load (input);


	# Function: save_data
	# -------------------
	# function to pickle all of the dicts we have
	def save_data (self):
		adj_vectors_filename = os.path.join(input_directory, '')


	# Function: constructor
	# ---------------------
	# will ensure that all dependencies and adj_vectors are loaded
	def __init__(self, input_directory=None, output_directory=None):

		self.input_directory = input_directory
		self.output_directory = output_directory

		if not (input_directory or output_directory):
			self.load_data ()
		else:
			print "---> Status: loading all dependencies"
			self.get_all_dependencies (input_directory)

			print "---> Status: getting adjective vectors"
			self.get_adj_vectors ()




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
	def get_all_dependencies (self, input_directory):

		self.dependencies = []

		for f in os.listdir(input_directory):
			xml_doc_name = os.path.join(input_directory, f)
			print "	---> loading from " + xml_doc_name

			tree = ET.parse (xml_doc_name);
			root = tree.getroot ();

			for dep in root.findall('.//dep'):
				governor = dep.find('governor')
				dependent = dep.find ('dependent')
				self.dependencies.append ((dep.attrib['type'], governor.text, dependent.text))




	# Function: get_adj_vectors
	# ------------------------
	# given a list of all dependencies, this will assemble
	# all 'adj_vector', which is a defaultdict(lambda: 0) that maps adjectives
	# to the number of times they modify the word
	def get_adj_vectors (self):

		self.adj_vectors = defaultdict(lambda:None)

		### Step 1: get raw counts ###
		print "	---> Status: getting raw counts"
		for dep in self.dependencies:
			dep_type = dep[0]
			governor = dep[1]
			dependent = dep[2]

			if dep_type == 'amod' or dep_type == 'appos' or dep_type == 'num':
				if not self.adj_vectors[governor]:
					self.adj_vectors[governor] = defaultdict (lambda: 0.0)
				self.adj_vectors[governor][dependent] += 1



		### Step 2: normalize ###
		print "	---> Status: normalizing"
		for word in self.adj_vectors.keys ():

			#--- get the total # of adjectives that have modified it ---
			total = 0.0
			for adjective in self.adj_vectors[word].keys():
				total += self.adj_vectors[word][adjective]

			#--- divide each entry appropriately ---
			for adjective in self.adj_vectors[word].keys():
				self.adj_vectors[word][adjective] = float(self.adj_vectors[word][adjective]) / total


	# Function: get_top_euphamism_candidates
	# ----------------------------------
	# this function will return a list of (word, similarity) tuples
	def get_top_euphamism_candidates (query_word, corpus):

		descriptor_counts =	get_descriptor_counts (query_word, corpus);







if __name__ == "__main__":

	#--- get options
	parser = optparse.OptionParser()
	parser.add_option ('-i', '--input-directory', help='directory containing all files to grab dependencies from')
	parser.add_option ('-o', '--output-directory', help='directory to dump all the pickled objects into')
	(opts, args) = parser.parse_args()


	# --- create euphamism_finder
	euphamism_finder = Euphamism_finder ('./data/input', './data/output')



	#--- get adj_vector for this word
	# print "---> Status: getting all adjective vectors..."
	# adj_vectors = get_adj_vectors (all_dependencies)










