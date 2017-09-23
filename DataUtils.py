import pandas as pd


characteristicts_data = pd.read_csv('/Users/admin/Documents/hackathon/mvidia/dataset2.csv', encoding='utf-8', na_filter=False)
comments_data = pd.read_csv('/Users/admin/Documents/hackathon/mvidia/dataset1.csv', encoding='utf-8', na_filter=False)

categories = comments_data.CATEGORY_ID.unique()
testing_categories = [
    1070907, #tv
    2030201, #notebook
    2050101, #smartphones
    4030101, #washing mashines
    #todo холодильники пылесосы посудомойки
]

def get_category_comments_data(id):
    return comments_data[comments_data['CATEGORY_ID'] == id]

def get_category_characteristicts_data(id):
    return characteristicts_data[characteristicts_data['CATEGORY_ID'] == id]

def get_unique_characteristics(data):
    return data["CODE"].unique()


