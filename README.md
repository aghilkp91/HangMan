# HangMan
HangMan game - a word guessing game - built using Python 

### Usage:
* Run ` make install ` to install the python dependencies
* Next run ` make run ` to run the game
* Can run ` make test ` to run unit test
* Can run ` make group ` to group word by charater count into a json file which is used to randomly generate the word

### Game Complexity
* Easiest - 25 Lives, character count between 6-8
* Easy - 10 Lives, character count between 5-10
* Normal - 7 Lives, character count between 5-13
* Hard - 3 Lives, character count between 10-24
* Nightmare - 1 Lives, character count between 15-24

### Word Generation
Currently I have copied the words from `/usr/share/dict/words` file of a unix system and grouped it by character count to make things easier. Tried using random_word module but it was giving lot of API error. But fixing that will help us get words with different difficulty level basd upon Corpus count too.


### Config changes
Word geenrator config file is at data/config.ini. The values can be changed there to change difficulty of words for random_word module.