from src.NGram import NGram
from src.TrainingSetHandler import TrainingSetHandler
from src.Predictor import Predictor
from src.OutputHelper import OutputHelper
from src.Constants import Constants
import string

def main():
    training_set = TrainingSetHandler()
    training_set.load_training_set()
    gram = NGram(3, 'ab', 0.5)
    gram.train("aaabbb", "gibberish")
    gram2 = NGram(3, 'ab', 0.5)
    gram2.train("aaabbb", "francais")
    predic = Predictor([gram, gram2])
    sentence = "aabb"
    prediction = predic.predict_this_sentence(sentence)
    with open("test.output", 'w') as f:
        output = OutputHelper(prediction, sentence, f)
        output.print_and_save_output()
    a = 0

if __name__ == '__main__':
    main()
