from src.NGram import NGram
from src.TrainingSetHandler import TrainingSetHandler
from src.Predictor import Predictor
import string

def main():
    training_set = TrainingSetHandler()
    training_set.load_training_set()
    gram = NGram(3, 'ab')
    gram.train("aaabbb", "gibberish")
    predic = Predictor([gram])
    prediction = predic.predict_this_sentence("hdfasjkdfhslajkfhdskljfhsdfjlkhsfljkhsajhafjlsahfsjaldfhsadfhsajfhsdfsdhafajksdlhf")
    a = 0

if __name__ == '__main__':
    main()
