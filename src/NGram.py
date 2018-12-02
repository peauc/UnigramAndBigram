import string

class NGram:
    def __init__(self, size, character_set):
        self.__size = size
        self.__gram = self.__make_default_gram(self.size, character_set)

    #region Properties
    @property
    def size(self):
        return self.__size
    #endregion

    def __make_default_gram(self, size, character_set):
            ret = dict()

            if size == 1:
                for idx, c in enumerate(character_set):
                    ret[c] = 0
                return ret
            for idx, c in enumerate(character_set):
                ret[c] = self.__make_default_gram(size - 1, character_set)
            return ret

    # TODO: Didn't find a way to pass the formating method to the function without rewriting one myself
    #  and i'm lazy so hardcoding for now
    def train(self, training_corpus):
        training_corpus = [c for c in training_corpus.lower() if c.isalpha()]
        grams = [training_corpus[i:i+self.size] for i in range(len(training_corpus)-self.size+1)]
        for g in grams:
            self._feed_grams(self.__gram, g)

    def _feed_grams(self, gram, g):
        if len(g) == 1:
            gram[g[0]] += 1
            return
        self._feed_grams(gram[g[0]], g[1:])




