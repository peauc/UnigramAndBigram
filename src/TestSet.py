from src.Constants import Constants

class TestSetHandler:
    #region Properties
    @property
    def test_set(self):
        return self.__test_set
    #endregion

    def __init__(self):
        self.__filename = Constants.TEST_FILE_RELATIVE_FILENAME
        self.__test_set = []

    def load_test_sentence(self):
        with open(self.__filename, 'r') as f:
            self.__test_set = enumerate(f.read().splitlines())

