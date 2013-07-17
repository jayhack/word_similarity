import os
import sys
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector


textfile_directory = "/Users/jhack/Programming/NLP/euphamisms/erotica_corpus/"


class DmozSpider(BaseSpider):
    name = "textfiles"
    allowed_domains = ["textfiles.com"]
    start_urls = [
    	"http://textfiles.com/sex/EROTICA/"
    ]


    # Function: get_text_file 
    # -----------------------
    # given a response from a text file, this will save it in 
    # the correct directory
    def get_text_file (self, response):

    	outfile_name = os.path.join(textfile_directory, response.meta['textfile_name']);

    	outfile = open (outfile_name, 'w')
    	outfile.write (response.body)
    	outfile.close ()
    	return



    # Function: parse_letter_page
    # ---------------------------
    # this function will get all the text files from a letter page
    def parse_letter_page (self, response):

    	print "########### parse letter page ##########"
    	hxs = HtmlXPathSelector (response);
    	filename_xpath = "//a/text()"
    	names = hxs.select (filename_xpath).extract()
    	
    	textfile_requests = []
    	for name in names:
    		new_url = response.url + name
    		meta = {'textfile_name':name}
    		textfile_requests.append (Request (url=new_url, callback=self.get_text_file, meta=meta))

    	return textfile_requests
			





    # Function: generate_start_letter_requests
    # ----------------------------------------
    # given the url to the erotica, this will return a list of requests for each
    # of the starting letter pages
    def generate_start_letter_requests (self, url):

    	alphabet_letters = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    	requests = []
    	for letter in alphabet_letters:
    		new_url = url + letter + '/'
    		requests.append(Request (url=new_url, callback=self.parse_letter_page))

    	return requests

    def parse(self, response):

    	return self.generate_start_letter_requests (response.url)