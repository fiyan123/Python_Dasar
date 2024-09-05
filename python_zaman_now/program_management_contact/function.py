
# daftar kontak
def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("========================")
        print(f"Nama     : {kontak['nama']}")
        print(f"Email    : {kontak['email']}")
        print(f"Nomor HP : {kontak['no_hp']}")
        print("========================")

def new_kontak():
    nama = input("Masukkan Nama : ")
    email = input("Masukkan Email : ")
    no_hp = input("Masukkan Nomor HP : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "no_hp" : no_hp
    }

    return kontak

def hapus_kontak(daftar_kontak):

    telepon = input("Masukkan Nomor Telepon Yang Akan Dihapus : ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak['no_hp']:
            index = i
            break
    if index == -1:
        print("=== Data Kontak Tidak Ditemukan! ===")
    else:
        del daftar_kontak[index]
        print("=== Berhasil Menghapus Data Kontak! ===")

def cari_kontak(daftar_kontak):
    email_dicari = input("Masukkan Email Kontak Yang Dicari : ")
    found = False

    for kontak in daftar_kontak:
        email_kontak = kontak["email"]
        if email_dicari in email_kontak:
            print("========================")
            print(f"Nama     : {kontak['nama']}")
            print(f"Email    : {kontak['email']}")
            print(f"Nomor HP : {kontak['no_hp']}")
            print("========================")
            found = True

    if not found:
        print("=== Kontak Yang Dicari Tidak Ada ===")
