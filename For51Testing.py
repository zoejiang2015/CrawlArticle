# -*-coding=utf8-*-
import sys
reload(sys)
# sys.setdefaultencoding('utf8')

import urllib2
from pip._vendor.distlib.locators import Page
from bs4 import BeautifulSoup
import re
import MySQLdb


def connect_db():
    global conn
    global cur 
    conn = MySQLdb.connect(host="localhost", user = "root", passwd ="qa1234" , db="crawlarticle", charset='utf8')
    cur = conn.cursor()
    return cur   
           
def sql_insert(cur, sql):
    result = cur.execute(sql)
    conn.commit()
    return result                
                    
 
def getPage(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    page = response.read()
    return page
    
    
def getSoup(url):
    page = getPage(url)    
    soup = BeautifulSoup(page, "html.parser", from_encoding="gb18030")
    
    return soup

def pageAnalysis(url):
    soup_ob = getSoup(url)
    print soup_ob.find_all('Div')


def read_url(key):
    sub_soup = getSoup(key)
#     if catid != None:
#         print catid.group()
    pattern_id= re.compile(r'catid.\d+') 
    catid = re.search(pattern_id, key).group().encode('utf-8')
    for content in sub_soup.find_all('ul'):
#         print content
#         print '*****************************************I am the gorgeous split line ***********************************************'
#         print type(content)
#         print content
#         print str(content)
        pattern=re.compile(r'<ul class=".+"')
        result = re.search(pattern, str(content))
        if result != None :
            pattern1 = re.compile(r'\"')
            result1 = re.split(pattern1, result.group())
            print result1[1]
            for li in content.find_all('li'):
                for a in li.find_all('a'):
                    title = a.get_text().encode('utf-8')
                    href = a.get('href').encode('utf-8')
                    if href.decode('utf-8').find('itemid') > -1:
                    
                        if catid == 'catid_32':
                            print '*********************************************no title***************************************'
                            pass
                        else:
                            sql = 'INSERT INTO originarticles(article, URL, source, keywords, catid)VALUES("%s", "%s", "51 Testing", "测试", "%s")' %(title, href, catid)
                            sql_insert(cur, sql)
        
                        
  
  
        
if __name__ == '__main__':
    global result_dict
    result_dict = dict()
    url = "http://www.51testing.com/html/index.html"
#     For51Testing.pageAnalysis(url)
    soup = getSoup(url)
    articleNum = 0
    titles = [] 
    hrefs = []
    cur = connect_db()   
#     print soup.find_all('ul')
    for content in soup.find_all('ul'):
#         print content
#         print '*****************************************I am the gorgeous split line ***********************************************'
#         print type(content)
#         print content
#         print str(content)
        pattern=re.compile(r'<ul class=".+"')
        result = re.search(pattern, str(content))
        if result != None :
#             print '*****************************************I am the gorgeous split line ***********************************************'
            pattern1 = re.compile(r'\"')
            result1 = re.split(pattern1, result.group())
#             print result1[1]
            for li in content.find_all('li'):
                for a in li.find_all('a'):
                    title = a.get_text().encode('utf-8')
                    href = a.get('href').encode('utf-8')
                    keyword = u"测试"
                    if title.decode('utf-8').find(keyword) > -1:
                        # add the url to repository for crawl
                        if href.find('itemid') > -1:
#                             sql = 'INSERT INTO originarticles(article, URL, source, keywords)VALUES("%s", "%s", "51 Testing", "测试")'  %(title, href)
#                             sql_insert(cur, sql)
                            pass
                        elif href.find('catid') > -1:
#                             print href.find('catid')
#                             print href
                            
                            result_dict[href] = title
                                
    for key in result_dict:
        print '*****************************************I am the gorgeous split line ***********************************************'
        print key
        read_url(key)
#         pattern_id= re.compile(r'catid.\d+') 
#         catid = re.search(pattern_id, key).group()
#         list = read_url(key)
#         title =  list[0]
#         href =  list[1]
#         print title
#         print href
#         print catid
#         sql = 'INSERT INTO originarticles(article, URL, source, keywords, catid)VALUES("%s", "%s", "51 Testing", "测试", "%s")' %(title, href, catid)
#         sql_insert(cur, sql)
#         except:
#             print '***************** Error Start'
#             pass
#             print '***************** Error End'
#            



    conn.close()                       

                           
            
                 

                    
                    
                    
                    
                    
                    
                    
                    
                    