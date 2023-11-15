# Casting merubah satu tipe data ke tipe data lain
# tipe data int, float, str, bool


# DATA INTEGER
print("===== INTEGER =====")
data_int = 10
print("Data = ", data_int, ", type = ", type(data_int))

# Diubah
data_float  = float(data_int)
data_str    = str(data_int)
data_bool   = bool(data_int) # akan false jika 0

print("Data = ", data_float, ", type = ", type(data_float))
print("Data = ", data_str, ", type = ", type(data_str))
print("Data = ", data_bool, ", type = ", type(data_bool))


# DATA FLOAT
print("===== FLOAT =====")
data_float = 9.5
print("Data = ", data_float, ", type = ", type(data_float))

# Diubah
data_int   = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float) # akan false jika 0

print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_str, ", type = ", type(data_str))
print("Data = ", data_bool, ", type = ", type(data_bool))


# DATA BOOLEAN
print("===== BOOLEAN =====")
data_bool = False
print("Data = ", data_bool, ", type = ", type(data_bool))

# Diubah
data_int   = int(data_bool)
data_str   = str(data_bool)
data_float = float(data_bool) # akan false jika 0

print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_str, ", type = ", type(data_str))
print("Data = ", data_float, ", type = ", type(data_float))


# DATA STRING
print("===== STRING =====")
data_str = "10"
print("Data = ", data_str, ", type = ", type(data_str))

# Diubah
data_int   = int(data_str)
data_bool  = bool(data_str)
data_float = float(data_str) # akan false jika 0

print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_bool, ", type = ", type(data_bool))
print("Data = ", data_float, ", type = ", type(data_float))
