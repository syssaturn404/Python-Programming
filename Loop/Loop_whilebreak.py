# Contoh perulangan menggunakan break
jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    if(jawab == 'tidak'):
        break

print ("Total perulangan: "+ str(hitung))
