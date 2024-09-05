# Seputar Set

# list => [] bisa memasukkan data yang sama
# tuple => () sama dengan list bisa memasukkan data yang sama
# set => {} hanya memasukkan data unik ketika ada data yang sama maka data itu akan dihapus, 
#           untuk set tidak bisa mengakses data menggunakan index, posisi index nya bisa berubah
#           hanya bisa add dan remove saja

# contoh set{}

nama = {"adi", "enda", "rudi"}

nama.add("kemal")
print(nama)
print("")

for data in nama:
    print(data)
