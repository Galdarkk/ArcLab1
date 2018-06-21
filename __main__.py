import parser.request as req
import parser.parse_xml as xml
import parser.articles as art
import parser.counter as count
import os

if __name__ == '__main__':
    links = xml.parse_links(os.path.join(os.getcwd(), 'links'))
    xmls = req.read_links(links)
    next_links = xml.parse_xmls(xmls)
    words = art.get_articles(next_links)
    table = count.table
    for word in words:
        try:
            table[word] += 1
        except KeyError:
            continue

    xml.write_words(table, os.path.join(os.getcwd(), 'counted.file_reader.xml'))
    print('DONE')
