# downlink图片欲加载
import requests
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

# 拉取图片
def download_pic(pic_url):
	pass

# 检查路径
def check_path(path):
	pass

# 创建文件夹
def make_dir(path):
	pass

# 拉取配置
def get_config():
	pass

if __name__ == '__main__':
	for item in pic_src['sources']:
		url_dict = item['url']
		for key in url_dict.keys():
			split_item = url_dict[key].split('//')[1].split('/')
			base_url = split_item[0]
			file_name = split_item[-1]
			dir_path = split_item[1:-2]
			print(url_dict[key],base_url,dir_path,file_name)
