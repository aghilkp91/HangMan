from random_word import RandomWords
import configparser
import os
import random
import json

class WordClass:

    configFilePath = os.getcwd() + '/data/config.ini'
    word_dictionary_file_path = os.path.dirname(os.path.abspath(__file__)) + '/words_dict.json'
    words_dictionary = {}
    with open(word_dictionary_file_path) as f:
         words_dictionary = json.load(f)

    # Get a random word from random_word module
    def getRandomWord(minLength, maxLength, maxCorpusCount):
        # Reading from config parser
        config = configparser.ConfigParser()
        config.read(WordClass.configFilePath)
        # Get a random word from dictionary
        r = RandomWords()
        flag = True
        while (flag):
            # word = r.get_random_word(hasDictionaryDef=config['Words']['HASDICTIONARYDEF'], includePartOfSpeech=config['Words']['INCLUDEPARTOFSPEECH'], minCorpusCount=config['Words']['MINCOPRPUSCOUNT'], 
            #         maxCorpusCount=maxCorpusCount, minDictionaryCount=config['Words']['MINDICTIONARYCOUNT'], maxDictionaryCount=config['Words']['MAXDICTIONARYCOUNT'],
            #         minLength=minLength, maxLength=maxLength)
            word = r.get_random_word()
            # print(word)
            if word:
                flag = False
        return word

    def getRandomWordFromList(min_length, max_length, max_corpus_count):
        word_length = random.randint(min_length, max_length)
        return random.choice(WordClass.words_dictionary[str(word_length)])


    