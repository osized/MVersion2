from DataUtils import *
for key, value in get_category_comments_data(2050101):
    print(str(key) + ": [")
    for v in value.CATEGORY_ID.unique():
        print(str(v) + ",")
    print("]")