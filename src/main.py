from src.NGram import NGram
from src.TrainingSetHandler import TrainingSetHandler
from src.Predictor import Predictor
from src.OutputHelper import OutputHelper
from src.Constants import Constants
from src.TestSet import TestSetHandler
from src.ConfigurationHandler import ConfigurationHandler
import string
import os

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
