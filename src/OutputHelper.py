from src.Constants import Constants

class OutputHelper:

    def __init__(self, predictions, sentence):
        self.__idx = 0
        self.__predictions = predictions
        self.__sentence = sentence

    def __get_model_name(self, size):
        if size in Constants.MODEL_NAMES:
            return Constants.MODEL_NAMES[size]
        else:
            return "{}Gram".format(size)

    def __print_title(self, n, sentence):
        print(sentence)
        print("{} Model:".format(self.__get_model_name(n).upper()))

    def __compute_and_print_probabilities(self, n, languages):
        # I was trying to get every item n by n
        while (len([0]) > 0):
            for l, values in languages.items():
                val = values[0]

    def __print_footer(self, winner):
        pass

    def print_and_save_output(self):
        for n, language in self.__predictions.items():
            self.__print_title(n, self.__sentence)
            winner = self.__compute_and_print_probabilities(n, language)
            self.__print_footer(winner)





