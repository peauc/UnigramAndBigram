from src.Constants import Constants


class Utils:
    @staticmethod
    def format_gram_to_joint_probability(param):
        splitter = ""
        if len(param) != 1:
            splitter = "|"
        return param[:1] + splitter + param[1:]

    @staticmethod
    def get_model_name(size):
        if size in Constants.MODEL_NAMES:
            return Constants.MODEL_NAMES[size]
        else:
            return "{}Gram".format(size)
