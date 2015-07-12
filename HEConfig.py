import os

from newspaper import Config

# urls item format: url,type,regex_for_links,tags
# type can be article,articles,feed
# regex_for_links is python regex to match links
# tags is seperated by :

class HEConfig(Config):

    def __init__(self):
        Config.__init__(self)
        self.memoize_articles = False
        self.fetch_images = False
        self.request_timeout = 60
        self.number_threads = 20
        self.keep_article_html = True
        self.MIN_WORD_COUNT = 20
        self.verbose = True
        self.keep_article_html = True

        self.urls = {
        'category1': [
        'a_url,articles,a_regex_for_links,a_tags',
        'b_url,article,,b.tags',
        'c_url,feed,,c.tags'
         ],
        }
        self.outputDir = 'content' + os.sep + 'category'
        self.max_number = 2000
        self.max_days = 100
