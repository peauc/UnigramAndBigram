import string
from src.Utils import Utils


class NGram:
    def __init__(self, size, character_set, delta):
        self.__size = size
        self.__total_number_of_grams = 0
        self.__gram = self.__make_empty_gram(self.size, character_set, delta)
        self.__language = ""

    #region Properties
    @property
    def language(self):
        return self.__language

    @property
    def total_number_of_grams(self):
        return self.__total_number_of_grams

    @total_number_of_grams.setter
    def total_number_of_grams(self, value):
        self.__total_number_of_grams = value

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

    def predict(self, ngram):
        return ngram, 0

    def _feed_grams(self, gram, g):
        if len(g) == 1:
            self.__total_number_of_grams += 1
            gram[g[0]] += 1
            return
        self._feed_grams(gram[g[0]], g[1:])

    def __make_empty_gram(self, size, character_set, delta):
        ret = dict()

        if size == 1:
            for idx, c in enumerate(character_set):
                ret[c] = delta
                self.__total_number_of_grams += delta
            return ret
        for idx, c in enumerate(character_set):
            ret[c] = self.__make_empty_gram(size - 1, character_set, delta)
        return ret



