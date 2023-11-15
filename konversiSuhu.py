# Program Contoh Konversi celcius ke satuan lain

print("")
print("=================================")
print("\n PROGRAM KONVERSI TEMPERATUR \n")
print("=================================")
print("")

celcius = float(input("Masukkan Suhu Dalam Celcius : "))
print("")
print("Suhu Yang Dimasukkan : ", celcius, "Celcius") 
print("")

# REAMUR
# (4/5) * C
reamur = (4/5) * celcius
print("Suhu Dalam Reamur Adalah : ", reamur, "Reamur")

# FAHRENHEIT
fahrenheit = ((9/5) * celcius) + 32
print("Suhu Dalam Fahrenheit Adalah : ", fahrenheit, "Fahrenheit")

# KELVIN
kelvin = celcius + 273
print("Suhu Dalam Kelvin Adalah : ", kelvin, "Kelvin")

print("")
print("===== Fahrenheit Ke Kelvin =====")
# Fahrenheit ke Kelvin
data_fk = (fahrenheit - 32) * 5/9 + 273.15
print("Suhu Dalam Fahrenheit Ke Kelvin Adalah : ", data_fk, "Kelvin")

print("")
print("===== Kelvin Ke Fahrenheit =====")
# kelvin ke fahrenheit
data_kf = (kelvin - 273.15) * 9/5 + 32
print("Suhu Dalam Kelvin Ke Fahrenheit Adalah : ", data_kf, "Fahrenheit")
