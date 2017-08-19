import re

html = """
<p>safari 5.1 – MAC<br>User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X
10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1
Safari/534.50</p>
<p>safari 5.1 – Windows<br>User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1;
en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50</p>
<p>IE 9.0<br>User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1;
Trident/5.0;</p>
<p>IE 8.0<br>User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0;
Trident/4.0)</p>
<p>IE 7.0<br>User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)</p>
<p>IE 6.0<br>User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)</p>
<p>Firefox 4.0.1 – MAC<br>User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X
10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1</p>
<p>Firefox 4.0.1 – Windows<br>User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1)
Gecko/20100101 Firefox/4.0.1</p>
<p>Opera 11.11 – MAC<br>User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8;
U; en) Presto/2.8.131 Version/11.11</p>
<p>Opera 11.11 – Windows<br>User-Agent:Opera/9.80 (Windows NT 6.1; U; en)
Presto/2.8.131 Version/11.11</p>
<p>Chrome 17.0 – MAC<br>User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X
10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56
Safari/535.11</p>
<p>傲游（Maxthon）<br>User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;
Maxthon 2.0)</p>
<p>腾讯TT<br>User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;
TencentTraveler 4.0)</p>
<p>世界之窗（The World） 2.x<br>User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows
NT 5.1)</p>
<p>世界之窗（The World） 3.x<br>User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows
NT 5.1; The World)</p>
<p>搜狗浏览器 1.x<br>User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;
Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X
MetaSr 1.0)</p>
<p>360浏览器<br>User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;
360SE)</p>
<p>Avant<br>User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant
Browser)</p>
<p>Green Browser<br>User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT
5.1)</p>
<p>移动设备端：</p>
<p>safari iOS 4.33 – iPhone<br>User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS
4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko)
Version/5.0.2 Mobile/8J2 Safari/6533.18.5</p>
<p>safari iOS 4.33 – iPod Touch<br>User-Agent:Mozilla/5.0 (iPod; U; CPU iPhone
OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko)
Version/5.0.2 Mobile/8J2 Safari/6533.18.5</p>
<p>safari iOS 4.33 – iPad<br>User-Agent:Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like
Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2
Mobile/8J2 Safari/6533.18.5</p>
<p>Android N1<br>User-Agent: Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus
One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile
Safari/533.1</p>
<p>Android QQ浏览器 For android<br>User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U;
Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1
(KHTML, like Gecko) Version/4.0 Mobile Safari/533.1</p>
<p>Android Opera Mobile<br>User-Agent: Opera/9.80 (Android 2.3.4; Linux; Opera
Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10</p>
<p>Android Pad Moto Xoom<br>User-Agent: Mozilla/5.0 (Linux; U; Android 3.0;
en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0
Safari/534.13</p>
<p>BlackBerry<br>User-Agent: Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en)
AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile
Safari/534.1+</p>
<p>WebOS HP Touchpad<br>User-Agent: Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0;
U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6
TouchPad/1.0</p>
<p>Nokia N97<br>User-Agent: Mozilla/5.0 (SymbianOS/9.4; Series60/5.0
NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525
(KHTML, like Gecko) BrowserNG/7.1.18124</p>
<p>Windows Phone Mango<br>User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows
Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)</p>
<p>UC无<br>User-Agent: UCWEB7.0.2.37/28/999</p>
<p>UC标准<br>User-Agent: NOKIA5700/ UCWEB7.0.2.37/28/999</p>
<p>UCOpenwave<br>User-Agent: Openwave/ UCWEB7.0.2.37/28/999</p>
<p>UC Opera<br>User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; )</p>
"""
def get_agent_arr():
	user_agent_arr = re.compile('<br>(.*?)</p>').findall(html.replace('\n',''))
	arr =[]
	for user_agent in user_agent_arr:
		try:
			name,address= user_agent.split(':')
			name = name.strip()
			address = address.strip()
			arr.append(address)
		except Exception as e:
			print(e)
	return arr