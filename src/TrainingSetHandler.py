from src.ConfigurationHandler import ConfigurationHandler
from src.Constants import Constants
import os

# By default this class load the default configuration file
class TrainingSetHandler:
    def __init__(self):
        self.__configuration_handler = ConfigurationHandler()
        self.__languages_path = []
        self.__training_set = {}
        self.__is_training_set_loaded = False

    #region Properties
    @property
    def language_list(self):
        return self.__configuration_handler.languages

    @property
    def training_set(self):
        return self.__training_set

    @property
    def is_training_set_loaded(self):
        return self.__is_training_set_loaded
    #endregion

    def _read_configuration_file(self, configuration_file=None):
        if configuration_file is not None:
            self.__configuration_handler.configuration_file = configuration_file
        self.__languages_path = self.__configuration_handler.get_langages_folder_absolute_path()

    def _read_lines_from_folder(self, folder_path):
        lines = ""
        for file in os.listdir(folder_path):
            if file.endswith(Constants.VALID_TRAINING_FILE_EXTENTION):
                with open(os.path.join(folder_path, file), "r") as f:
                    text = f.read()
                    lines += text
        return lines

    def _load_data(self):
        for idx, fp in enumerate(self.__languages_path):
            self.__training_set[self.language_list[idx]] = self._read_lines_from_folder(fp)
        self.__is_training_set_loaded = True

    def load_training_set(self, configuration_file=None):
        self._read_configuration_file(configuration_file)
        self._load_data()
