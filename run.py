#!/usr/bin/python
# -*- coding: UTF-8 -*-
import exec
import sys
import datetime
import os

import sys
#p1=sys.argv[1]
#p2=sys.argv[2]

#print('获取到参数：{p1:'+p1+','+'p2:'+p2+'}')
p1 = input("请选择下载模式：\n 1.normal \n 2.下载自定义页面视频 \n 3.下载单个视频 \n")

print('开始下载')
startTime = datetime.datetime.now()
#如果第一个参数==0，根据第二参数链接下载视频
if int(p1) == 1:
    print('normal')
    category = exec.getCategory()
    str_page = str(exec.getPage())
    types = {'rf':'最近加精','top':'本月最热','tf':'本月收藏','mf':'收藏最多','long':'10分钟','longer':'20分钟','hf':'高清','md':'本月讨论'}
    file_path = types[category]+'-'+str_page
    print(file_path)
    page_url ='http://807.workgreat17.live/v.php?category='+category+'&viewtype=basic&page='+str_page
    print(page_url)
    exec.download(page_url,file_path)
    
elif int(p1) == 2:
    p2 = input('请输入视频页面链接：\n')
    exec.download(p2,'dim-1')
else:
    p2 = input('请输入视频链接：\n')
    exec.downloadvideo(p2,'dim-1')
print('下载完成')
print('上传文件到Onedrive')

date = datetime.datetime.now().strftime('%Y%m%d')
date_time = datetime.datetime.now().strftime('%Y%m%d-%H%M')

#配置文件位置根据实际位置修改
up_cmd = 'OneDriveUploader -f -c "/content/mdowm-main/auth2.json" -s "./videos/"'+date+' -r "video/m3u8download/"'
print(up_cmd)
os.system(up_cmd)

print('上传完成')
print('删除videos下文件')

delete_cmd = "rm -rf ./videos/*"
os.system(delete_cmd)
print('Done..')
endTime = datetime.datetime.now()
seconds = (endTime- startTime).seconds
print('下载共耗时：%d秒' %(seconds))
