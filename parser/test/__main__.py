from parser.test import articles_test
from parser.test import request_test
from parser.test import xml_test

if __name__ == '__main__':
    print('Tests for package: "file_reader" started ...')
    print(xml_test.parse_links_test())
    print(request_test.read_links_test())
    print(xml_test.parse_xml_test())
    print(xml_test.parse_xmls_test())
    print(xml_test.write_words_test())
print('Tests for package: successfully passed')