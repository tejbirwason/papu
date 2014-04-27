# Scrapy settings for papu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'papu'

SPIDER_MODULES = ['papu.spiders']
NEWSPIDER_MODULE = 'papu.spiders'

ITEM_PIPELINES = {'papu.files.FilesPipeline'}

FILES_STORE = 'Users/tejbirwason/Desktop/scrapy'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'papu (+http://www.yourdomain.com)'
