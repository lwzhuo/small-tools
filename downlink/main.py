# downlink图片欲加载
import requests
from pathlib import Path
import os
import json

# 图片来源数据
pic_src = {
	"sources": [
		{
			"name": "GOES-East Full Disk",
			"spacecraft": "GOES-East",
			"interval": 900,
			"aspect": 1,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/678x678.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/5424x5424.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/latest.jpg"
			}
		},{
			"name": "GOES-West Full Disk",
			"spacecraft": "GOES-West",
			"interval": 900,
			"aspect": 1,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/FD/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/FD/GEOCOLOR/678x678.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/FD/GEOCOLOR/5424x5424.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/FD/GEOCOLOR/latest.jpg"
			}
		},{
			"name": "Himawari-8 Full Disk",
			"spacecraft": "Himawari-8",
			"interval": 900,
			"aspect": 1,
			"url": {
				"tiny": "http://rammb.cira.colostate.edu/ramsdis/online/images/thumb/himawari-8/full_disk_ahi_true_color.jpg",
				"small": "http://rammb.cira.colostate.edu/ramsdis/online/images/latest/himawari-8/full_disk_ahi_true_color.jpg",
				"large": "http://rammb.cira.colostate.edu/ramsdis/online/images/latest_hi_res/himawari-8/full_disk_ahi_true_color.jpg",
				"full": "http://rammb.cira.colostate.edu/ramsdis/online/images/latest_hi_res/himawari-8/full_disk_ahi_true_color.jpg"
			}
		},{
			"name": "Continental US",
			"spacecraft": "GOES-East",
			"interval": 300,
			"aspect": 1.667,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/625x375.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/5000x3000.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/latest.jpg"
			}
		},{
			"name": "Tropical Atlantic",
			"spacecraft": "GOES-East",
			"interval": 900,
			"aspect": 1.667,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/GEOCOLOR/900x540.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/GEOCOLOR/3600x2160.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/GEOCOLOR/latest.jpg"
			}
		},{
			"name": "Tropical Pacific",
			"spacecraft": "GOES-West",
			"interval": 900,
			"aspect": 1.667,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/tpw/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/tpw/GEOCOLOR/900x540.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/tpw/GEOCOLOR/3600x2160.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/tpw/GEOCOLOR/latest.jpg"
			}
		},{
			"name": "US West Coast",
			"spacecraft": "GOES-West",
			"interval": 900,
			"aspect": 1.667,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/CONUS/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/CONUS/GEOCOLOR/625x375.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/CONUS/GEOCOLOR/5000x3000.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/CONUS/GEOCOLOR/latest.jpg"
			}
		},{
			"name": "Northern Pacific",
			"spacecraft": "GOES-West",
			"interval": 900,
			"aspect": 1.667,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/np/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/np/GEOCOLOR/900x540.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/np/GEOCOLOR/7200x4320.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/np/GEOCOLOR/latest.jpg"
			}
		},{
			"name": "Northern South America",
			"spacecraft": "GOES-East",
			"interval": 900,
			"aspect": 1.667,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nsa/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nsa/GEOCOLOR/900x540.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nsa/GEOCOLOR/3600x2160.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nsa/GEOCOLOR/latest.jpg"
			}
		},{
			"name": "Southern South America",
			"spacecraft": "GOES-East",
			"interval": 900,
			"aspect": 1.667,
			"url": {
				"tiny": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/ssa/GEOCOLOR/thumbnail.jpg",
				"small": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/ssa/GEOCOLOR/900x540.jpg",
				"large": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/ssa/GEOCOLOR/3600x2160.jpg",
				"full": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/ssa/GEOCOLOR/latest.jpg"
			}
		}
	]
}

# 图片的基础路径
base_path = '/Users/zhuo/Desktop/pic_path/'

# 处理单张图片整个流程
def handle(pic_url):
	# 分割url
	split_item = pic_url.split('//')[1].split('/')
	base_url = split_item[0]
	file_name = split_item[-1]
	dir_path = split_item[1:-2]
	print(url_dict[key], base_url, dir_path, file_name)
	target_dir_path = base_path + os.sep.join(dir_path)

	check_path(target_dir_path)
	# pic_url = 'https://himg.bdimg.com/sys/portraitn/item/830ca1ef6ca1ef77a1ef7aa1eff10f'
	pic_bin = download_pic(pic_url)
	save_pic(pic_bin,target_dir_path,file_name)

# 拉取图片
def download_pic(pic_url):
	print('开始下载图片:'+pic_url)
	resp = requests.get(pic_url)
	print('图片下载完毕')
	return resp.content

def save_pic(img_bin,dir_path,file_name):
	print("开始保存图片:"+file_name)
	f = open(dir_path+os.sep+file_name,'wb')
	f.write(img_bin)
	f.close()
	print("保存图片["+file_name+"]完毕")

# 检查路径
def check_path(path):
	pic_path = Path(path)
	if not pic_path.exists(): # 路径不存在或者路径对应的不是文件夹 创建文件夹
		os.makedirs(path)
		print("创建路径:" + path)
	else:
		if not pic_path.is_dir():
			raise Exception("目标路径不是文件夹")
		else:
			print("路径检查完毕:"+path)


# 在线拉取配置
def get_config():
	resp = requests.get("https://downlinkapp.com/sources.json")
	content = resp.text
	content = json.loads(content)
	return content

if __name__ == '__main__':
	# get_config()
	for item in pic_src['sources']:
		url_dict = item['url']
		for key in url_dict.keys():
			handle(url_dict[key])
