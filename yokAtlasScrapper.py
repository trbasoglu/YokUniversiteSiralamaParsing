from bs4 import BeautifulSoup as bs
import requests

r = requests.get("https://yokatlas.yok.gov.tr/tercih-sihirbazi-t4-tablo.php?p=say")

source = bs(r.content, "html.parser")
print(source)
rows = source.find_all("tbody")
for row in rows:
    print(row)
    print("*********************")