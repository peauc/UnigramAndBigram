from src.NGram import NGram
from src.TrainingSetHandler import TrainingSetHandler
from src.Predictor import Predictor
from src.OutputHelper import OutputHelper
from src.Constants import Constants
import string

def main():
    training_set = TrainingSetHandler()
    training_set.load_training_set()
    gram = NGram(3, 'ab')
    gram.train("aaabbb", "gibberish")
    gram2 = NGram(1, 'ab')
    gram2.train("aaabbb", "gibberish")
    predic = Predictor([gram, gram2])
    prediction = predic.predict_this_sentence("hdfasjkdfhslajkfhdskljf hsdfjlkhsfljkhsajhafjlsahfsjaldfhsadfhsajfhsdfsdhafajksdlhf")
    output = OutputHelper()
    output.print_and_save_output(prediction)
    a = 0

if __name__ == '__main__':
    main()
