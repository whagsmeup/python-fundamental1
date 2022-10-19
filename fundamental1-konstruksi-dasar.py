# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: EKSEKUSI BERURUTAN
print("Hello World!")
print("By WhagsMeUp")
print("Tanggal 19 Oct 2022")
print('-' * 25)

#PERCABANGAN: EKSEKUSI TERPILIH
ingin_cepat = True
if ingin_cepat:
    print('Jalan Lurus Ya!')
else:
    print('Jalan Lain')

#PERULANGAN
jumlah_anak = 4

for index_anak in range(0, jumlah_anak): #jumlah perulangan = 5 - 1 = 4
    print(f'Halo anak #{index_anak}')