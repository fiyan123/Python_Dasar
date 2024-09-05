# Argument List 
# contoh argument list diparameter (*list_angka), disimpan di akhir ketika banyak parameter

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")

jumlahkan(10, 10, 10,20, 220)