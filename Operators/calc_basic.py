import os

# deklarasi fungsi penjumlahan
def add(x, y):
    return x + y

# deklarasi fungsi pengurangan
def subtract(x, y):
    return x - y

# deklarasi fungsi perkalian
def multiplay(x, y):
    return x * y

# deklarasi fungsi pembagian
def divide(x, y):
    return x / y

# daftar menu
os.system('clear')
print('.:: CALCULATOR SEDERHANA ::.\n')
print('Daftar Menu ::')
print('[1]. Penjumlahan')
print('[2]. Pengurangan')
print('[3]. Perkalian')
print('[4]. Pembagian')

# ambil input user
pil = input('Masukan MENU : ')

bil_1 = int(input('Bilangan Pertama : '))
bil_2 = int(input('Bilangan Kedua : '))

#conditional
if pil == '1':
    print('Hasil', bil_1,'+', bil_2, '=', add(bil_1, bil_2))
elif pil == '2':
    print('Hasil', bil_1,'-', bil_2, '=', subtract(bil_1, bil_2))
elif pil == '3':
    print('Hasil', bil_1,'*', bil_2, '=', multiplay(bil_1, bil_2))
elif pil == '4':
    print('Hasil', bil_1,'/', bil_2, '=', divide(bil_1, bil_2))
