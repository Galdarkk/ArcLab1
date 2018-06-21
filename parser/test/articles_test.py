import parser.articles as art


def pure_word_test():
    test_res = '\tucityt.parser.articles.pure_word test'
    try:
        assert art.pure_word('привіт') is True
        assert art.pure_word('12345') is False
        return '✔ passed' + test_res
    except AssertionError:
        return '✘ not passed' + test_res

def gen_list_test():
    test_res = '\tucityt.parser.articles.gen_list test'
    text = 'привіт,друг, ,, , як це я'
    expected_words = ['привіт', 'друг', '', '', '', '', '', '', 'як', 'це', 'я']
    try:
        assert art.gen_list(text) == expected_words
        return '✔ passed' + test_res
    except AssertionError:
        return '✘ not passed' + test_res


def get_words_test():
    test_res = '\tucityt.parser.articles.get_words test'
    text = 'привіт,друг, ,, , як це я'
    expected_words = ['привіт', 'друг', 'це']
    try:
        assert art.get_words(text) == expected_words
        return '✔ passed' + test_res
    except AssertionError:
        return '✘ not passed' + test_res
