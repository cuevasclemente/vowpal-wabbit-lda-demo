#!/usr/bin/python3
import requests as rq
import nltk.data
import sys
import re
from bs4 import BeautifulSoup

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

wikipedia_base = "http://en.wikipedia.org/wiki/"

wikipedia_pages = ["mathematics", "poetry", "continent", "vegetable"]


lda_topics = len(wikipedia_pages)

if len(sys.argv) > 1 and sys.argv[1] == "topics":
    print(lda_topics)
    exit(0)

training_set = []
for page in wikipedia_pages:
    req = rq.get("{}{}".format(wikipedia_base, page))
    soup = BeautifulSoup(req.text, 'html.parser')
    paragraphs = soup.find_all("p")
    raw_paragraphs = map(lambda x: x.text, paragraphs)
    for paragraph in raw_paragraphs:
        # tokenizer will give us real sentences
        sentences = tokenizer.tokenize(paragraph)
        for sentence in sentences:
            # Let's get rid of wikipedia footnotes
            # as a first bit of cleaning
            line = re.sub("\[[0-9]*\]", "", sentence)
            # Next, we have to remove colons, this is a special
            # issue with vowpal wabbit. It would probably be better
            # to use a regular snowball-stemmer or something else
            line = re.sub("\:", "", line)
            # Skip empty sentences
            line = line.strip()
            if not line:
                continue
            print("|raw "+line)
exit(0)
