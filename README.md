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

kemudian menggunakan sqlite3 untuk membuat database dan tabel sesuai kolom yang kita inginkan
