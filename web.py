import requests
from bs4 import BeautifulSoup
import sqlite3

src = "https://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht"
page = requests.get(src)
soup = BeautifulSoup(page.content, 'html.parser')

koneksi = sqlite3.connect ('imdb.db')
koneksi.execute ('''create table if not exists film
                 (judul text not null,
                 weekend text not null,
                 gross text not null);''')

variabel = soup.find(class_='chart full-width')
imdb = variabel.findAll ('tr')
imdb.pop(0)
for i in range (len(imdb)):
    judul = imdb[i].find (class_='titleColumn')
    judul = judul.getText()
    judul = judul.split('\n')[1]
    weekend = imdb[i].find (class_='ratingColumn')
    weekend  = weekend.getText()
    weekend = weekend.split()[0]
    gross = imdb[i].find (class_='secondaryInfo')
    gross = gross.getText()
    koneksi.execute ('insert into film values ("%s","%s","%s")' %(judul,weekend,gross))

cetak = koneksi.execute ("select * from film")
for i in cetak:
    print (i)
