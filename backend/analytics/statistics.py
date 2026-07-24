from collections import Counter


def category_statistics(skills):

    categories = [
        skill["category_code"]
        for skill in skills
    ]

    return Counter(categories)