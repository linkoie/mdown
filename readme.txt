pip install -r requirements.txt

sudo apt install -y ffmpeg

视频下载方法：
1.爬取指定视频，传入参数{p1:'v',p2:'site_addr'}
eg: python run.py 'v' 'https://807.workgreat17.live/view_video.php?viewkey=542c22e81f44adb7f661&page=&viewtype=&category='
2.爬取指定页面全部视频，传入页码参数{p1:1,p2:0}
eg；python run.py 1 0
3.爬取指定页面全部视频，传入页面地址{p1:0,p2:'site_addr'} 本月最热
eg；python run.py 0 'https://807.workgreat17.live/v.php?category=top&viewtype=basic&page=1'     #本月最热
	python run.py 0 'https://807.workgreat17.live/v.php?category=tf&viewtype=basic&page=1'	    #本月收藏
	python run.py 0 'https://807.workgreat17.live/v.php?category=rf&viewtype=basic&page=2'	    #最近加精
	python run.py 0 'https://807.workgreat17.live/v.php?category=mf&viewtype=basic&page=2'	    #收藏最多
	python run.py 0 'https://807.workgreat17.live/v.php?category=long&viewtype=basic&page=2'    #10分钟
	python run.py 0 'https://807.workgreat17.live/v.php?category=longer&viewtype=basic&page=2'  #20分钟
	python run.py 0 'https://807.workgreat17.live/v.php?category=hf&viewtype=basic&page=2'      #高清
	
