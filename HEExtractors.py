from newspaper import ContentExtractor,Parser
import lxml.html
import re
from datetime import datetime

class SinaBlogExtractor(ContentExtractor):

    def __init__(self,config):
        ContentExtractor.__init__(self,config)

    def get_authors(self, doc):
        nodes = Parser.xpath_re(doc,'//*[@id="ownernick"]')
        if len(nodes) > 0:
            s = Parser.getText(nodes[0])
            print("authors: " + s)
            return [s]

        return []

    def get_publishing_date(self, url, doc):
        def parse_date_str(date_str):
            try:
                #datetime_obj = date_parser(date_str)
                datetime_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                return datetime_obj
            except Exception as e:
                print(e)
                return None

        nodes = Parser.xpath_re(doc,'//*[@id="articlebody"]/div[1]/span')
        if len(nodes) > 0 :
            s = Parser.getText(nodes[0])
            s = re.sub('[\(\)]','',s)
            print("publish_date: " + s)
            return parse_date_str(s)

        return None

    def calculate_best_node(self, doc):
        #print(lxml.html.tostring(doc))  #doc.text_content()
        top_nodes = Parser.xpath_re(doc,'//*[@id="sina_keyword_ad_area2"]')
        if len(top_nodes) < 1:
            top_node = ContentExtractor.calculate_best_node(self,doc)
        else:
            top_node = top_nodes[0]
        #print(Parser.getText(top_node))
        #if top_node is None:
        #    return doc
        return top_node
