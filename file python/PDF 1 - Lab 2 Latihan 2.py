#Program Mengurutkan Bilangan Sederhana
angka = list()
jumlah = input("Masukan Jumlah Bilangan: ")
for i in range(int(jumlah)):
    n = input("Masukan Bilangan :")
    angka.append(n)
    angka.sort()
print("Bilangan Berurutan: ",*angka, sep= " ")
