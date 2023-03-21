import requests

url = 'http://143.110.160.221:30925/flag'

for i in range(0, 1001):
	
	res = requests.get(url);
	if 'HTB' in res.text or 'htb' in res.text:
		print(res.text)