import string
from src.Utils import Utils

class NGram:
    def __init__(self, size, character_set):
        self.__size = size
        self.__gram = Utils.make_empty_gram(self.size, character_set)
        self.__language = ""

    #region Properties
    @property
    def language(self):
        return self.__language

    @property
    def size(self):
        return self.__size
    #endregion

    # TODO: Didn't find a way to pass the formating method to the function without rewriting one myself
    #  and i'm lazy so hardcoding for now
    def train(self, training_corpus, language):
        self.__language = language
        training_corpus = [c for c in training_corpus.lower() if c.isalpha()]
        grams = [training_corpus[i:i+self.size] for i in range(len(training_corpus)-self.size+1)]
        for g in grams:
            self._feed_grams(self.__gram, g)

    def predict(self, character):

        return character, 0

    def _feed_grams(self, gram, g):
        if len(g) == 1:
            gram[g[0]] += 1
            return
        self._feed_grams(gram[g[0]], g[1:])




