from xml.etree import ElementTree as etree


def parse_links(path):
    return list(map(lambda node: node.text, etree.parse(path).getroot()))


def parse_xml(xml):
    return [item.find('link').text for item in etree.fromstring(xml).find('channel').findall('item')]


def parse_xmls(xmls):
    return [link for xml in xmls for link in parse_xml(xml)]


def write_words(cities_dic, output_file):
    words_node = etree.Element('cities')
    for word in cities_dic:
        word_node = etree.SubElement(words_node, 'city')
        text_node = etree.SubElement(word_node, 'name')
        count_node = etree.SubElement(word_node, 'count')
        text_node.text = word
        count_node.text = str(cities_dic[word])
    etree.ElementTree(words_node).write(output_file, 'utf-8')
