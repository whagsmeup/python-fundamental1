"""
Tipe data dictionari = menghubungkan KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak':'son', 'istri':'wife', 'ayah':'father', 'ibu':'mother'}
print(kamus_ind_eng)
print(kamus_ind_eng["ayah"])
print(kamus_ind_eng["ibu"])

print('\n Data ini dikirim oleh server Gohjek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_server_gojek = {'Tanggal': '2022-09-08',
                     'driver_list':[
                         {'nama':'Whag','jarak':12},
                         {'nama':'Gieg','jarak':14},
                         {'nama':'Elly','jarak':1},
                         {'nama':'Eko','jarak':100},
                     ]}

print(data_server_gojek)
print(f"\n Driver Di Sekitar Sini {data_server_gojek['driver_list']}")
print(f"Driver #1 {data_server_gojek['driver_list'][0]}")
print(f"Driver #2 {data_server_gojek['driver_list'][1]}")
print(f"Driver Terdekat Berjarak {data_server_gojek['driver_list'][1]['jarak']}")

