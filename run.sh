#!/bin/sh

./get_data.py > training_set

word_count=$(cat training_set | sed "s/|raw //" | tr -s " " "\n" | uniq | wc -l)

# The bitsize for vw is 2^18, says 
# http://mlwave.com/tutorial-online-lda-with-vowpal-wabbit/
# So we want a bit size that is
# ceil(log(word_count, 2))
# Now, to get the log base two, we have to use 
# change of base unfortunately. log_2(x) == ln(x) / ln(2)

num_bits=$(echo "(l($word_count)) / l(2)" |\
  bc -l |\
  # We need to ceiling now
  awk '{if(int($1) > 0) {print(int($1)-1)} else {print(1) } }')

vw --lda $(./get_data.py topics) -d training_set --readable_model wiki_model -b "$num_bits" 

./interpret_data.py
