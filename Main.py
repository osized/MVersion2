import DataUtils
import VectorizationUtils
import SearchUtils
from NormalizationUtils import *
from customDicts import get_keywords

for test_category in DataUtils.testing_categories:
    category_comments_data = DataUtils.get_category_comments_data(test_category)
    category_characteristics_data = DataUtils.get_category_characteristicts_data(test_category)
    category_TEXT_data = category_comments_data['TEXT']
    category_BENEFITS_data = category_comments_data['BENEFITS']

    for word, listCharNumbers in get_keywords(test_category).items():
        print(word + ": ")
        count = 0
        total = 0
        for row in category_BENEFITS_data:
            total += 1
            if VectorizationUtils.comment_contains_characteristic(row, word):
                count+=1
        print("WORD " + word + ": " + str(count)+"/"+str(total))



