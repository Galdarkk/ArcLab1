from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()


def base_form(word):
    return morph.parse(word)[0].normal_form
