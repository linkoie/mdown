import requests
import time

headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
    }
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
    