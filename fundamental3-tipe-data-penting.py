print('Tipe data saklar = tipe data sederhana');
anak1 = 'Whag'
anak2 = 'Gie'
anak3 = 'Khoirul'
anak4 = 'Leha'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\n Tipe data list/daftar/array')
anak = ['Whag','Gie','Trie','Leha']
print(anak)
anak.append('Khoirul')
print(anak)

print('\n Sapa anak pertama')
print(f'Hi {anak[0]}')

print('\n Sapa semua anak')
for a in anak:
    print(f'Hi {a}!!')

print('\n Sapa semua anak: cara ribet')
for a in range(0,len(anak)):
    print(f'Hi {anak[a]}!!!!')