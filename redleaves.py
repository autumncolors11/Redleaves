from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://kanko.city.kyoto.lg.jp/feature/momijidayori.php'
html = urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, 'html5lib')

# prettifyで整形されたファイルで保存
with open('migoro2018.html', mode = 'w', encoding = 'utf-8') as fw:
    fw.write(soup.prettify())