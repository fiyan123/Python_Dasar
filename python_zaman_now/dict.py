# Belajar Tipe Data Dictionary

customer = {"Name" : "Eko", "Age" : 30, "Address" : "Majalaya"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

# add
customer["company"] = "X"

# edit
customer["Address"] = "Timpa Alamat"

# delete
del customer["Address"]

for key, value in customer.items():
    print(f"{key} : {value}")

