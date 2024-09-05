# for loop list dan range

banyak = int(input("Berapa Banyak Data ? "))

nama = []
umur = []

for i in range(0, banyak):
    print(f"Data Ke {i}")
    input_nama = input("Masukkan Nama : ")
    input_umur = int(input("Masukkan Umur : "))

    nama.append(input_nama)
    umur.append(input_umur)

print("")

print("========================")
for a in range(0, len(nama)):
    data_nama = nama[a]
    data_umur = umur[a]
    print(f"{data_nama} berumur {data_umur} tahun")
print("========================")