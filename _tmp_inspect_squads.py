import requests
import csv
url = 'https://raw.githubusercontent.com/jfjelstul/worldcup/master/data-csv/squads.csv'
text = requests.get(url, timeout=15).text
reader = csv.reader(text.splitlines())
for _ in range(4):
    print(next(reader))
