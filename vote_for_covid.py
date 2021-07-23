import requests
import string
import random
def getHTTP(url):
	try:
		ran=''.join(random.sample(string.ascii_letters + string.digits, 7))
		users={'Accept': 'application/json, text/javascript, */*; q=0.01',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 10; '+ran+' Build/HUAWEICLT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/2644 MicroMessenger/7.0.12.1620(0x27000C36) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
		'X-Requested-With': 'XMLHttpRequest',
		'Origin': 'http://wxapi.junpinghui.com',
		'Referer': 'http://wxapi.junpinghui.com/huanqiutou/index.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
		'Cookie': 'UM_distinctid=17ad27c42e933c-00cee5d35de7f2-7a697f6d-144001-17ad27c42eab9f; CNZZDATA1260748058=1613979088-1627024598-%7C1627024599'
		}
		r=requests.post(url,timeout=30,headers=users)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "产生异常"

url1='http://wxapi.junpinghui.com/huanqiutou/vote.php'

demo=getHTTP(url1)
print(demo)
