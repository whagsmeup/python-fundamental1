"""
Program perulangan baca buku dengan for
"""

jumlah_buku = 10
print('Ibu berkata "Baca semua bukumu"')

jumlah_buku_terbaca = 0

for jumlah_buku_terbaca in range(1,jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_terbaca} yang sudah dibaca")

print(f"Jumlah buku yang sudah di baca {jumlah_buku_terbaca}")