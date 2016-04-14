# vw-lda

A simple demonstration of vowpal wabbit's LDA model (perhaps unsuccessful right now)

`$ ./run.sh `

# What you need to run this
## Programs
vowpal wabbit 

Available through many package mangers (i.e: `brew`, `apt`, etc.), and relatively easy to compile 

`$ git clone https://github.com/JohnLangford/vowpal_wabbit`

Then, you should be able to just `make` it. You may need to install `libboost` from your package provider as well but that should be it.

There are also some unix utils I guess not everyone has:
- `sed(1)`
- `awk(1)`
- `tr(1)`
- `bc(1)`


## Python requirements (availble to the runtime, either through a virtualenv, or installed on your system)
- requests
- nltk
- bs4
- nltk.data:"tokenizers/punkt/english.pickle" 
`$ python3 -m nltk.downloader punkt`
