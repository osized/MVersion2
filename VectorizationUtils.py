import gensim
from gensim import matutils
from numpy.core.multiarray import dot

from NormalizationUtils import get_dict_words

w2v_fpath = "/Users/admin/Documents/hackathon/mvidia/all.norm-sz100-w10-cb0-it1-min100.w2v"
w2v = gensim.models.KeyedVectors.load_word2vec_format(w2v_fpath, binary=True, unicode_errors='ignore')
w2v.init_sims(replace=True)

def vectorize_array(array):
    arr_vec = []
    for word in array:
        vec = vectorize_word(word)
        if vec:
            arr_vec.append(vec)
        else:
            print("WORD NOT IN DICT... " + word)
    return arr_vec

def vectorize_word(word):
    if word in w2v.wv.vocab:
        return w2v.wv[word]

def distance(vec1, vec2):
    return dot(matutils.unitvec(vec1), matutils.unitvec(vec2))

def comment_contains_characteristic(comment, characteristic):
    words = get_dict_words(comment)
    for word in words:
        if characteristic in w2v.wv.vocab and word in w2v.wv.vocab:
            score = w2v.wv.similarity(word, characteristic)
            if score > 0.8:
                return True
        else:
            return word.lower() == characteristic.lower()
    return  False