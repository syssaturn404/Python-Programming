# Contoh perulangan dengan while
jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input('Apakah kamu ingin mengulang ? ')

print('Total perulangan-', str(hitung))
