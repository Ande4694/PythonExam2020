import subprocess
import os
import requests


t = requests.get('http://keaplan.kea.dk/sws/prod2019/default.aspx')

print(t.text)

subprocess.run(['open', t])











