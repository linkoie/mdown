import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from bs4 import  BeautifulSoup
import os

def visit(url):
    retries = Retry(total=5,backoff_factor=10, status_forcelist=[500,502,503,504])
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9,eo;q=0.8'
        }
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=retries))
    response = s.get(url, headers=headers, stream=True)
    return response
#获取网页标题
def getTitle(url):
    html = visit(url).text
    soup = BeautifulSoup(html,'html.parser')
    page_title = soup.find('title').text.replace(" ","").replace("\n","").replace('Chinesehomemadevideo','')
    return page_title
if __name__ == '__main__':
    test_url = 'https://google.com'
    html = visit(test_url).text
    #print(html)
    title = getTitle(test_url)
    print(title)

def delete(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")
