from src.Constants import Constants
from src.Utils import Utils

from cmath import log

class OutputHelper:

    def __init__(self, predictions, sentence, file):
        self.__reset(predictions, sentence, file)

    def __reset(self, predictions, sentence, file):
        self.__lines_printed = 0
        self.__predictions = predictions
        self.__file = file
        self.__sentence = sentence
        self.__scores = {}

    def __get_model_name(self, size):
        if size in Constants.MODEL_NAMES:
            return Constants.MODEL_NAMES[size]
        else:
            return "{}Gram".format(size)

    def __print_title(self, n, sentence):
        model = "{} Model:".format(self.__get_model_name(n).upper())
        print(sentence)
        print(model)
        self.__file.write(sentence)
        self.__file.write(model)

    def __should_print(self, values_array):
        tester = ""

        for k, v in values_array.items():
            tester = k
            values_array[k] = v[1:]
        if (len(values_array[tester]) < 1):
            return False
        return True

    def __update_score_for_language(self, language, score):
        print("scores: ", self.__scores)
        print("score:", score[1])
        self.__scores[language] = self.__scores.get(language, 0) + log10(score[1])
        return self.__scores[language]

    def __track_and_print_probabilities(self, n, values_by_language):
        values_array = {language: values for (language, values) in values_by_language.items()}
        # We want to consume the first element of the first array, except the first time we enter the loop
        while self.__lines_printed == 0 or self.__should_print(values_array):
            for language, results in values_array.items():
                total_score = self.__update_score_for_language(language, results[0])
                self.__print_lines(language, results[0], total_score)
                self.__lines_printed += 1

    def __print_lines(self, language, unigramProbability, total_score):
        print("{}: P({}) = {}  ==> log prob of this sentence so far: {}".
              format(language.upper(), Utils.format_gram_to_joint_probability(unigramProbability[0]), unigramProbability[1], total_score))
        self.__file.write("{}: P({}) = {}  ==> log prob of this sentence so far: {}".
              format(language.upper(), Utils.format_gram_to_joint_probability(unigramProbability[0]), unigramProbability[1], total_score))


    def __print_footer(self, n, language):
        winner = self.__find_winner(language)
        print("According to the {} model, this sentence is in {}".format(self.__get_model_name(n), winner))
        self.__file.write("According to the {} model, this sentence is in {}".format(self.__get_model_name(n), winner))
        pass

    def print_and_save_output(self):
        for n, language in self.__predictions.items():
            self.__print_title(n, self.__sentence)
            self.__track_and_print_probabilities(n, language)
            self.__print_footer(n, language)

    def __find_winner(self, language):
        return max(zip(language.values(), language.keys()))[1].capitalize()






