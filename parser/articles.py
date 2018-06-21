import newspaper
import parser.morph as mrh
import re

delimiters = '\n| |,|\.|\?|\!|\:|\(|\)'
deletes = '^до|та|як|де|про|не|так|або|що|за|через|те|крім|того|на$'
delim = re.compile(delimiters)
filter_words = re.compile(deletes)


def process_article(link):
    article = newspaper.Article(url=link, language='uk')  # type: Article
    try:
        article.download()
        article.parse()
    except newspaper.ArticleException:
        return ''
    return article.text


def pure_word(word):
    return all(str.isalpha(c) for c in word)


def gen_list(text):
    return list(map(lambda word: word.lower() if isinstance(word, str) else '', delim.split(text)))


def get_words(text):
    return list(filter(
        lambda w: w != '' and pure_word(w) and len(w) >= 2 and not filter_words.match(w), gen_list(text)
    ))


def get_articles(links):
    return [mrh.base_form(word) for link in links for word in get_words(process_article(link))]
