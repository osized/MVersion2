from DataUtils import *
from customDicts import get_keywords
for key, value in get_category_comments_data(2050101).groupby("CATEGORY_NAME"):
    for v in value.CATEGORY_NAME.unique():
        print(str(v))
print(get_keywords(2050101))
