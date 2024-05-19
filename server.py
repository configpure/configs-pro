import requests

x = requests.get('https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/vless')

data = x.text.splitlines()

file = open('user1' , mode='w')
for line in data :
        datas = line.split("#")
        datas = datas[0] + "#Maghaze\n"
        file.write(datas)

file.close()