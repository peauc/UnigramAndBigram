from Constants import Constants
import sys
import os


# By default this class will assume that the default config file is data/.config
class ConfigurationHandler:

    def __init__(self):
        self.__configuration_file = os.path.join(Constants.CONFIG_PATH, Constants.CONFIG_FILE_NAME)
        self.__loaded = False
        self.__languages = []

    # region Properties
    @property
    def languages(self):
        return self.__languages

    @property
    def is_loaded(self):
        return self.__loaded

    @property
    def configuration_file(self):
        return self.__configuration_file

    @configuration_file.setter
    def configuration_file(self, new_file):
        self.__configuration_file = new_file

    # endregion

    # This method read the file set as self.__configuration_file and return the path of the training set to read
    def get_langages_folder_absolute_path(self):
        try:
            with open(self.configuration_file, 'r') as f:
                self.__loaded = True
                training_folder_relative_path = os.path.join(Constants.CONFIG_PATH, Constants.TRAINING_DATA_FOLDER)
                self.__languages = f.read().splitlines()
                # We use the relative data folder path from Constants to join to each file to get their absolute path
                return [os.path.join(os.path.abspath(training_folder_relative_path), i) for i in self.__languages]
        except FileNotFoundError as e:
            print("ConfigurationHandler couldn't find the configuration at path {}, your curent working directory is {}"
                  .format(self.configuration_file, os.getcwd()))
            pass
        except:
            print("Unexpected error: ", sys.exc_info()[0])
            raise
