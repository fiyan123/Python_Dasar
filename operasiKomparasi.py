# Operasi Komparasi

a = 5
b = 3

print("")

# Lebih besar dari > 
print("===== Lebih Besar Dari (>) =====")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)

print("")

# Kurang dari < 
print("===== Kurang Dari (<) =====")
hasil_kurang = a < 3
print(a, '<', 3, '=', hasil_kurang)
hasil_kurang = b < 3
print(b, '<', 3, '=', hasil_kurang)

print("")

# lebih besar sama dengan >=
print("===== Lebih Besar Sama Dengan (>=) =====")
hasil = a >= 3
print(a,'>=', 3, '=', hasil)
hasil = b >= 3
print(b,'>=', 3, '=', hasil)

print("")

# Kurang dari sama dengan <=
print("===== Kurang Dari Sama Dengan (<=) =====")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)

print("")

# Sama dengan (==)
print("===== Sama Dengan Dari (==) =====")
hasil = a == 3
print(a, '==', 3, '=', hasil)
hasil = b == 3
print(b, '==', 3, '=', hasil)

print("")

# tidak Sama dengan (!=)
print("===== Tidak Sama Dengan Dari (!=) =====")
hasil = a != 3
print(a, '!=', 3, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)

print("")


# is
# komprasi object identity
print("===== Object Identity (is & is not) =====")
x = 5
y = 5

print('nilai x = ',x,'id = ', hex(id(x)))
print('nilai y = ',y,'id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)