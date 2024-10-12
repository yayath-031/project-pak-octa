# Himaaaa

Package ini untuk mencari referensi Film, Game, Komik, Lagu, Novel, dan Series.

## Installation

Kamu bisa instal package ini menggunakan pip:

```bash
pip install himaaaa
```
## Fitur
- Mencari Komik berdasarkan Genre, Penulis, Tahun Terbit, dan Bahasa.
- Mencari Lagu berdasarkan Genre, Bahasa, dan Nama Artis.
- Mencari Series berdasarkan Genre, Tahun Terbit, dan Bahasa.
- Mencari Film berdasarkan Genre, Tahun Terbit, dan Bahasa.
- Mencari Game berdasarkan Genre, Tahun Terbit, dan Developer.
- Mencari Novel berdasarkan Genre, Penulis, Tahun Terbit, dan Bahasa.

## Usage

```python
from himaaaa import (nama function)

# returns 'cari_komik'
cari_komik(kriteria, nilai, batas)

# returns 'cari_lagu'
cari_lagu(kriteria, nilai, batas)

# returns 'cari_series'
cari_series(kriteria, nilai, batas)

# returns 'cari_film'
cari_film(kriteria, nilai, batas)

# returns 'cari_game'
cari_game(kriteria, nilai, batas)

# returns 'cari_novel'
cari_novel(kriteria, nilai, batas)
```

## Example
```python
hasil = cari_komik("penulis", "Akira Toriyama", 5)
print(hasil)

hasil = cari_lagu("artis", "Tulus", 5)
print(hasil)

hasil = cari_series("bahasa", "Bahasa Indonesia", 5)
print(hasil)

hasil = cari_film("genre", "Action", 5)
print(hasil)

hasil = cari_game("developer", "Garena", 5)
print(hasil)

hasil = cari_novel("penulis", "tereliye", 5)
print(hasil)
```
