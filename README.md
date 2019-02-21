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
page = requests.get(src)
soup = BeautifulSoup(page.content, 'html.parser')
