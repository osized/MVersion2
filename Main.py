import DataUtils
import VectorizationUtils
import SearchUtils
import NormalizationUtils

for test_category in DataUtils.testing_categories:
    category_comments_data = DataUtils.get_category_comments_data(test_category)
    category_characteristics_data = DataUtils.get_category_characteristicts_data(test_category)
    category_TEXT_data = category_comments_data['TEXT']
    category_BENEFITS_data = category_comments_data['BENEFITS']
    category_DRAWBACKS_data = category_comments_data['DRAWBACKS']
    category_TEXT_vec_data = VectorizationUtils.vectorize_array(category_TEXT_data)
    category_BENEFITS_vec_data = VectorizationUtils.vectorize_array(category_BENEFITS_data)
    category_DRAWBACKS_vec_data = VectorizationUtils.vectorize_array(category_DRAWBACKS_data)
