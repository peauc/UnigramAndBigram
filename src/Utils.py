from src.Constants import Constants


class Utils:
    #TODO: THIS
    @staticmethod
    def format_gram_to_joint_probability(param):
        return param.replace("", "|")[1:-1]

    @staticmethod
    def get_model_name(size):
        if size in Constants.MODEL_NAMES:
            return Constants.MODEL_NAMES[size]
        else:
            return "{}Gram".format(size)
