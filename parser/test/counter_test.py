import parser.counter as counter


def count_words_test():
    counted_requested_content = counter.count_words(requested_content)
    assert counted_requested_content == 14, 'Count of cities "heroku" in requested content is not equal with expected count of them'
    return '\tfile_reader.counter.count_cities test'