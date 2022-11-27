import datetime
import re
import requests
import threading
import os
import shutil
import time
import ffmpeg

headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
    }

#proxies = {'https':'192.168.31.180:10809','http': '192.168.31.180:10809'}
    

sem=threading.Semaphore(8) #限制线程的最大数量为4个

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False
#下载ts文件
def save_ts(ts_url,ts_name,retry_times = 3):
    if retry_times < 1:
        print(ts_name+'下载失败')
        return
    filepath = './video_ts/'+ts_name
    try:
        ts_file = requests.get(ts_url,headers=headers).content
        #以二进制方式 追加写入
        with open(filepath,mode='wb') as f:
            f.write(ts_file)
    except Exception as err:
        print(ts_name+'下载出错，重试中。。。')
        time.sleep(3)
        retry_times = retry_times - 1
        save_ts(ts_url,ts_name,retry_times)

#合并ts文件
def mergets(ts_list,vedio_path):
    with open(vedio_path,mode='ab') as fw:
        for ts in ts_list:
            if os.path.exists('./video_ts/'+ts):
                fr = open('./video_ts/'+ts,mode='rb')
                content = fr.read()
                fw.write(content)
                fr.close()
            else:
                print(ts+'文件缺失')




# 多线程下载文件
def download(m3u8_dict,file_path): # {'title': 'test2', 'm3u8': 'https://cdn77.91p49.com/m3u8/647088/647088.m3u8'}
    url = m3u8_dict['m3u8']
    title = m3u8_dict['title']
    m3u8_seq = re.findall(r'(?<=m3u8/).*(?=/.*.m3u8)',url)[0]
    date = datetime.datetime.now().strftime('%Y%m%d')
    #创建文件保存目录
    mkdir('./videos/'+date+'/'+file_path)
    #创建ts文件保存目录
    mkdir('./video_ts')
    #文件路径
    vedio_path = './videos/'+date+'/'+file_path+'/'+title+'.mp4' 
    startTime = datetime.datetime.now()
    m3u8 = requests.get(url, headers=headers).text
    
    #解析m3u8文件中的ts文件名称
    # 去除不必要的注释
    ts_list = re.sub(r'http.*','',m3u8)
    ts_list = re.sub(r'#E.*','',ts_list).split()

    print('一共有'+str(len(ts_list))+'片')

    #手工创建线程池
    threads = []
 
    for ts in ts_list:  # 循环创建线程
        ts_url = 'https://cdn77.91p49.com/m3u8/'+m3u8_seq+'/'+ts #https://cdn77.91p49.com/m3u8/651065/6510650.ts
        thread = threading.Thread(target=save_ts,args=(ts_url,ts))
        threads.append(thread)
        thread.setDaemon(True)  # 给每个子线程添加守护线程
        sem.release()
    for t in threads:  # 循环启动线程
        sem.acquire()
        t.start()
    for t in threads:
        t.join(10)  # 设置子线程超时5秒

    #合并文件
    #mergets(ts_list,vedio_path)
    #update 使用ffmpeg来合并ts文件
    ffmpeg.merge('./video_ts',vedio_path)
    
    #合并文件后删除ts文件
    shutil.rmtree('./video_ts',ignore_errors=True)
    print(m3u8_seq+"下载完成")
    endTime= datetime.datetime.now()
    # 相减得到秒数
    seconds = (endTime- startTime).seconds
    print('共耗时：%d秒' %(seconds))

if __name__ == '__main__':
    m3u8_dict_eg = {'title': 'test2', 'm3u8': 'https://cdn77.91p49.com/m3u8/647088/647088.m3u8'}
    download(m3u8_dict=m3u8_dict_eg,file_path='dim-1')

