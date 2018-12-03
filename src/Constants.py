import string


class Constants:
    MODEL_NAMES = {1: "Unigram", 2: "Bigram", 3: "Trigram", 4: "Quadrigram"}
    CONFIG_FILE_NAME = ".config"
    CONFIG_PATH = "../data/"
    OUTPUT_PATH = "../data/out"
    TRAINING_DATA_FOLDER = "train"
    VALID_TRAINING_FILE_EXTENTION = (".txt", "")
    CHARACTER_SET = string.ascii_lowercase
    # This array defines the deepness of ngram
    SIZE_OF_GRAMS = [1, 2]
    TEST_FILE_RELATIVE_FILENAME = "../data/test/first10TestSentences.txt"

