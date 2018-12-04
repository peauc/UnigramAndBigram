class Utils:
    @staticmethod
    def make_empty_gram(size, character_set):
        ret = dict()

        if size == 1:
            for idx, c in enumerate(character_set):
                ret[c] = 0
            return ret
        for idx, c in enumerate(character_set):
            ret[c] = Utils.make_empty_gram(size - 1, character_set)
        return ret

    @staticmethod
    def format_gram_to_joint_probability(param):
        return param
