import common
import re
from bs4 import BeautifulSoup


m3u8_dict = {}

def getm3u8Addr(url): 
    title = common.getTitle(url).replace(' Chinese homemade video','')
    m3u8_dict['title']=title

    #m3u8 https://la.killcovid2021.com/m3u8/649351/649351.m3u8
    # for entry in browser.get_log('browser'):
    #     _url = entry['message']
    #     if '.m3u8' in _url:
    #         m3u8 = re.findall(r'.*.m3u8',_url)[0]
    #         print(_url)
    #         m3u8_dict['m3u8']=m3u8
    #         return m3u8_dict
    response = common.visit(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    m3u8 = soup.find('div',id='VID').text
    m3u8url='https://cdn77.91p49.com/m3u8/'+m3u8+'/'+m3u8+'.m3u8' #https://cdn77.91p49.com/m3u8/651065/651065.m3u8
    m3u8_dict['m3u8']=m3u8url
    return m3u8_dict



if __name__ == '__main__':
    base_url = "https://807.workgreat17.live/view_video.php?viewkey=542c22e81f44adb7f661&page=&viewtype=&category="
    print(getm3u8Addr(base_url))
    
