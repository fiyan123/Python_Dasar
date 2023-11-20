# OR (jika salah satu true, maka hasilnya adalah true)

print('===== OR =====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c )

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c )

a = True
b = False
c = a or b
print(a, 'OR', b, '=', c )

a = True
b = True
c = a or b
print(a, 'OR', b, '=', c )


print('')
# AND (jika dua buah nilai true maka hasil true)
print('===== AND =====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)
