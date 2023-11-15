# Tipe Data angka satuan gada komanya (integer)
data_integer = 1
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# Tipe Data float
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))

# Tipe Data string
data_string = "Hello World"
print("data : ", data_string, ", bertipe : ", type(data_string))

# Tipe Data biner true/false (boolean)
data_bool = True
print("data : ", data_bool, ", bertipe : ", type(data_bool))

## Tipe data Khusus
# Bilangan Kompleks
data_complex = complex(5,6)
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# Tipe Data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.6)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))


