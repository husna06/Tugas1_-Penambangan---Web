# Tugas1_ Crawling Data
Tugas : mengambil data teks di website menggunakan python kemudian disimpan di database

## Identitas 

> Nama : Husna
>
> NIM : 160411100018
>
> Matkul : Penambangan dan Pencarian Web 

## Pengantar

- [ ] Program ini menggunakan Bahasa Python dengan library :
  - Beautifulsoup4
  - requests
  - SQlite3 
- [ ] Mengambil data teks di Website (IMDb Top Box Office) : https://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht

## Penjelasan Program 
```
src = "https://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht"
page = requests.get(src)
soup = BeautifulSoup(page.content, 'html.parser')
```

> pada code diatas digunakan untuk mendowload html dari link web tersebut, kemudian 
> untuk variabel ``` soup ``` mengubah html ke object beautiful soup

setelah itu barulah kita bisa mecari teks yang mau kita ambil pada web tersebut, untuk contoh

tersebut kita mengambil `` judul`` , rating hasilnya pada hari `` weekend`` dan ``gross`` , dan untuk 

memperjelas tempat data yang mau kita ambil pahami terlebih dahulu di html web. 

```
for i in range (len(imdb)):
    #mangambil judul 
    judul = imdb[i].find (class_='titleColumn')
    #mengambil textnya saja 
    judul = judul.getText()
    #menghilangkan tab supaya tampilannya lebih cantik
    judul = judul.split('\n')[1]
    weekend = imdb[i].find (class_='ratingColumn')
    weekend  = weekend.getText()
    weekend = weekend.split()[0]
    gross = imdb[i].find (class_='secondaryInfo')
    gross = gross.getText()
```



`` judul = judul.getText()`` untuk mengambil textnya saja dan ``judul = judul.split('\n')[1]`` untuk

menghilangkan tab supaya tampilannya lebih cantik dan tetata rapi . 

kemudian menggunakan sqlite3 untuk membuat database dan tabel sesuai kolom yang kita inginkan
```
koneksi = sqlite3.connect ('imdb.db')
koneksi.execute ('''create table if not exists film
                 (judul text not null,
                 weekend text not null,
                 gross text not null);''')
```

