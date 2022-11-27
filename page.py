from pydoc import classname
import common
from bs4 import BeautifulSoup


def getPageurl(url):
    url_list = []
    response = common.visit(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    div_list = soup.find_all(name='div',attrs={'class':'videos-text-align'})
    for div in div_list:
        link = div.find('a')
        url = link['href']
        url_list.append(url)
    return url_list    
    

if __name__ == '__main__':
    test_url = 'https://807.workgreat17.live/v.php?category=rf&viewtype=basic&page=2'
    vedio_list = getPageurl(test_url)
    print(vedio_list)
