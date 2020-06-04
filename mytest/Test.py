import requests

# respone = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=' + '180.97.33.108')
respone = requests.get(('https://freeapi.ipip.net/'+'180.97.33.108'))
t = respone.text
print(t)