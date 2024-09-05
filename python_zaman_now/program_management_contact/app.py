# Management Contact Data

import function

# list dictionary
daftar_kontak = []

daftar_kontak.append({
    "nama" : "Kama",
    "email" : "kama@gmail.com",
    "no_hp" : "087218271872121"
})

# menu perulangan
while True:
    print("# Menu : ")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("Silahkan Pilih Menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
        print(" === Data Kontak Berhasil Di Tambah === ")
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else: 
        print("=== Menu Tidak Tersedia ===")
        
print("Program Selesai, Terima Kasih")
    
