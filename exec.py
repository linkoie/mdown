import time
import page
import parsem3u8
import m3u8download
import common
import datetime



def getPage():
    r = 0
    while True:
        num = input("请输入想爬的页数:")
        try:
            r = int(num)
            break
        except:
            print("抱歉，您输入的不是有效的数字, 请重新输入.")
            continue
    return r

def getCategory():
    category = 'dim'
    while True:
        num = input("请输入想爬的类别:\n 1.最近加精  2.本月最热 \n 3.本月收藏  4.收藏最多 \n 5.10分钟  6.20分钟 \n 7.高清 \n 8.本月讨论")
        try:
            r = int(num)
            break
        except:
            print("抱歉，您输入的不是有效的数字, 请重新输入.")
            continue
    categories = ['rf','top','tf','mf','long','longer','hf','md']
    category = categories[r-1]
    return category

#多线程下载
def dd_by_many_thread(url_list,file_path):
    fail_job_list= []
    date = datetime.datetime.now().strftime('%Y%m%d')
    for p_url in url_list:
        m3u8_dict = parsem3u8.getm3u8Addr(p_url)
        #使用m3u8downloder 下载
        try:
            m3u8download.download(m3u8_dict,file_path)
        except Exception as err:
            print('%s下载失败'%(m3u8_dict['title']))
            #写入失败任务列表
            fail_job_list.append(m3u8_dict)
            #删除文件
            title = m3u8_dict['title']
            common.delete('./videos/'+date+'/'+file_path+'/'+title+'.mp4')
            print(title+'.mp4'+'文件下载失败')
            continue   
        time.sleep(2)
#下载方法
def download(page_url,file_path):
    page_url_list = page.getPageurl(page_url)
    dd_by_many_thread(page_url_list,file_path)
    
def downloadvideo(url,file_path):
    m3u8_dict = parsem3u8.getm3u8Addr(url)
    m3u8download.download(m3u8_dict,file_path)

if __name__ == '__main__':
    category = getCategory()
    str_page = str(getPage())
    types = {'rf':'最近加精','top':'本月最热','tf':'本月收藏','mf':'收藏最多','long':'10分钟','longer':'20分钟','hf':'高清','md':'本月讨论'}
    file_path = types[category]+'-'+str_page
    print(file_path)
    page_base_url ='http://807.workgreat17.live/v.php?category='+category+'&viewtype=basic&page='+str_page
    print(page_base_url)
    page_url_list = page.getPageurl(page_base_url)
    dd_by_many_thread(page_url_list,file_path)

