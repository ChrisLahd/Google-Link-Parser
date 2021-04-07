import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector

import pandas as pd

class firstSpider(scrapy.Spider): 
  name = "basic" 
  start_urls = [ 
    # where "foobar" is placed in the next line, is where the keyword goes.
    "https://www.google.com/search?q=foobar"
   ]
   
  def parse(self, response):

    df = pd.DataFrame()
    xlink = LinkExtractor()
    
    link_list=[]
    link_text=[]
    
    divs = response.xpath('//div')
    text_list=[]
    
    for span in divs.xpath(''):
      if len(str(span.get()))>100:
        text_list.append(span.get())
    
    for link in xlink.extract_links(response):

      # where "or ''in" is mentioned in the next line is where filters can be made. in between '', place your desired output filter keyword.
      if len(str(link))>200 or ''in link.text:
        
        print(len(str(link)),link+"\n")
        link_list.append(link)
    
    for i in range(len(link_text)-len(text_list)):
    
      text_list.append(" ")
    df['links']=link_list
    df.to_csv('output.csv')
