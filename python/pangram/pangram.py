__author__ = 'afox'

def is_pangram(sentence):
    """
    Determine if a sentence is a pangram. A pangram (Greek: ??? ??????, pan gramma,
    "every letter") is a sentence using every letter of the alphabet at least once.
    The best known English pangram is "The quick brown fox jumps over the lazy dog."

    :param sentence: String "The quick brown fox jumps over the lazy dog."
    :return: Bool
    """

    return len(set(sentence)) > 26
