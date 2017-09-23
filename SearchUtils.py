import gensim
import  VectorizationUtils

w2v_fpath = "/Users/admin/Documents/hackathon/mvidia/all.norm-sz100-w10-cb0-it1-min100.w2v"
w2v = gensim.models.KeyedVectors.load_word2vec_format(w2v_fpath, binary=True, unicode_errors='ignore')
w2v.init_sims(replace=True)

def words_contains_in_text_AND(text_words_array, words_seq):
    for seq in words_seq:
        if not word_contains_in_text(text_words_array, seq):
            return False
    return True

def word_contains_in_text(text_words_array, word_seq):
    for word in text_words_array:
            score = VectorizationUtils.distance(word, word_seq)
            if score > 0.8:
                return True
    return False