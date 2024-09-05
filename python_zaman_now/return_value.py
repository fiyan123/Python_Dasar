# Mereturn value dari method ber parameter, dengan begitu hasil data program bisa dikembalikan

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka    
    return (list_angka, total)

list_angka, total = jumlahkan(10, 10, 10,20, 20)

print(f"Total {list_angka} = {total}")