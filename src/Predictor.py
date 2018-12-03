# Todo rename this class. His task is to get the result and return them so we can use them
class Predictor:
    #region Properties
    @property
    def sentences(self):
        return self.__sentences
    #endregion

    def __init__(self, grams):
        self.__grams = grams
        self.__sentences = {}

    def __pop_first_elements_of_sentence(self):
        for k, v in self.__sentences.items():
            if len(v) != 0:
                self.__sentences[k].pop(0)

    def __is_finished(self):
        for k, v in self.__sentences.items():
            if len(v) != 0:
                return False
        return True

    # Same as above the class definition
    def predict_this_sentence(self, sentence):
        sizes = set([g.size for g in self.__grams])
        ret = {size: {} for size in sizes}
        self.__sentences = {size: [sentence[i:i+size] for i in range(len(sentence)-size+1)] for size in sizes}
        while not (self.__is_finished()):
            for g in self.__grams:
                sentence = self.__sentences.get(g.size)
                if len(sentence) > 0:
                    ret[g.size].setdefault(g.language, []).append(g.predict(sentence[0]))
            self.__pop_first_elements_of_sentence()
        return ret
