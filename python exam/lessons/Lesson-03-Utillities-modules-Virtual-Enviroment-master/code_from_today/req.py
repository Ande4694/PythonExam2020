import requests


res = requests.get('http://keaplan.kea.dk/sws/prod2019/default.aspx')

text = res.text


print(text)
