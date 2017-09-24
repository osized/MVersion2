import re

def get_dict_words(text):
    sentence = []
    comment = text.lower().replace('ё', 'е')
    replaced_comment = re.sub('[^а-яa-z]', ' ', comment)
    for word in replaced_comment.split(' '):
        if word and not is_stop_word(word):
            sentence.append(word)
    return sentence

def normalize_all_data(array):
    return [get_dict_words(X) for X in array]

def is_stop_word(word):
    if word in ["для", "в", "с", "со", "от", "к"]:
        return True
    return  False