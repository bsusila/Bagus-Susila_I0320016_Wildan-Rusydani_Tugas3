# membuat dictionary
dict = {'nama': 'Bagus Susila',
        'hobi1': 'olahraga', 'hobi2': 'menonton film', 'hobi3': 'membaca',
        'sosmed1': 'ig:@bagususila', 'sosmed2': 'twitter:@bsusila_', 'sosmed3': 'line:@bagususila_',
        'lagufavorit1': 'Imagine', 'lagufavorit2': 'Yellow', 'lagufavorit3': 'Sorry',
        'makananfavorit1': 'nasi goreng', 'makananfavorit2': 'mie ayam', 'makananfavorit3': 'burger'}

# mengubah salah satu hobi dan sosmed
dict['hobi3'] = 'muncak'
dict['sosmed3'] = 'tiktok:@bagussusila'

# menghapus 2 makanan favorit, dan menambah 1 hobi
del dict['makananfavorit2']
del dict['makananfavorit3']
dict['hobi4'] = 'main game'

print(dict)
