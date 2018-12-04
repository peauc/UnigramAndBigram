from NGram import NGram
from TrainingSetHandler import TrainingSetHandler
from Predictor import Predictor
from OutputHelper import OutputHelper
from Constants import Constants
from TestSet import TestSetHandler
from ConfigurationHandler import ConfigurationHandler
from Utils import Utils
import string
import os
import math


def go_down_recursively(gram, file, total, actual_gram):
    for letter, value in gram.items():
        if isinstance(value, float):
            file.write("P({}) = {}\n".format(Utils.format_gram_to_joint_probability(actual_gram + letter), (value/total)))
        else:
            go_down_recursively(value, file, total, actual_gram + letter)


def dump_grams(grams):
    for gram in grams:
        language_identifier = "ot"
        if gram.language in Constants.LANGUAGE_TABLE:
            language_identifier = Constants.LANGUAGE_TABLE[gram.language]
        filename = Utils.get_model_name(gram.size).lower() + language_identifier.upper() + ".txt"
        with open(os.path.join(Constants.OUTPUT_PATH, filename), 'w') as f:
            go_down_recursively(gram.gram, f, gram.total_number_of_grams, "")


def main():
    training_set = TrainingSetHandler()
    training_set.load_training_set()
    gram_list = []

    for size in Constants.SIZE_OF_GRAMS:
        for language in training_set.language_list:
            gram = NGram(size, string.ascii_lowercase, 0.5)
            gram.train(training_set.training_set[language], language)
            gram_list.append(gram)

    #dump copies of grams to file
    dump_grams(gram_list)

    predic = Predictor(gram_list)
    test_set_handler = TestSetHandler()
    test_set_handler.load_test_sentence()
    for idx, sentence in enumerate(test_set_handler.test_set):
        clean_sentence = "".join([c for c in sentence[1] if c.isalpha()]).lower()
        prediction = predic.predict_this_sentence(clean_sentence)
        with open(os.path.join(Constants.OUTPUT_PATH, "out{}.txt".format(idx)), 'w') as f:
            output = OutputHelper(prediction, sentence, f)
            output.print_and_save_output()

if __name__ == '__main__':
    main()
