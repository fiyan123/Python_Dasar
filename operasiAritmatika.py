# Contoh Operasi Aritmatika

a = 10
b = 5

# operasi tambah + 
hasil_tambah = a + b
print(a, '+', b, '=', hasil_tambah)

# operasi pengurangan -
hasil_pengurangan = a - b
print(a, '-', b, '=', hasil_pengurangan)

# operasi perkalian *
hasil_perkalian = a * b
print(a, '*', b, '=', hasil_perkalian)

# operasi pembagian /
hasil_pembagian = a / b
print(a, '/', b, '=', hasil_pembagian)

# operasi eksponen(pangkat) **
hasil_pangkat = a ** b
print(a, '**', b, '=', hasil_pangkat)

# operasi hasil modulus %
hasil_persen = a % b
print(a, '%', b, '=', hasil_persen)

# operasi hasil floor division (kebalikan modulus) //
hasil_floor = a // b
print(a, '//', b, '=', hasil_floor)


# Prioritas Operasi, Operational Precedence

'''
    1. ()
    2. exponen **
    3. perkalian dan lainnya * / ** % //
    4. pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=' , hasil)

# Kurung di eksekusi dahulu
hasil_2 = x + (y * z)
print(x,'+ (',y,'*',z, ') =', hasil_2)