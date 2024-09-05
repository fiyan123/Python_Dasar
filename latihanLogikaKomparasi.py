# # Membuat gabungan area rentang dari angka

# # +++++++3----------------10++++++++++++++
# # kurang dari 3 lebih dari 10 
# # Operator Or

# inputUser = float(input("\n Masukkan Angka Yang bernilai \n Kurang dari 3 \n atau \n Lebih Besar dari 10 : "))

# # Memeriksa apakah kurang dari 3
# print("")
# isKurangDari = (inputUser < 3)
# print("Kurang Dari 3 = ",isKurangDari)

# isLebihDari = (inputUser > 10)
# print("Lebih Dari 10 = ",isLebihDari)

# isCorrect = isKurangDari or isLebihDari
# print("Angka Yang Anda Masukkan = ",isCorrect)


# # lebih dari 3 kurang dari 10
# # kasus irisan Operator and
# print("\n========================================")
# inputUser = float(input("\n Masukkan Angka Yang bernilai \n Lebih dari 3 \n dan \n Kurang dari 10 : "))

# # -----3++++++++10-----
# print("")
# isLebihDari = inputUser > 3
# print("Lebih Dari 3 = ",isLebihDari)

# isKurangDari = inputUser < 10
# print("Kurang Dari 10 = ",isKurangDari)

# isCorrect = isLebihDari and isKurangDari
# print("Angka Yang Anda Masukkan = ", isCorrect)

# ------- 0 ++++++++++ 5 ------------ 8 +++++++++++++ 11 ---------
# +++++++ 0 ---------- 5 ++++++++++++ 8 ------------- 11 +++++++++
print("")
print("==============================")
print("Latihan Komparasi Logikanya")
print("==============================")

print("")
inputUser = float(input("Masukkan Angka 0 - 5, dan 8 - 11 : "))
rules1 = inputUser < 0
rules2 = inputUser > 5
rules3 = inputUser < 8
rules4 = inputUser > 11

jawaban1 = rules1 and rules2 or rules3 and rules4
print("jawabannya adalah :", jawaban1) 

print("")
inputUser = float(input("Masukkan Angka Lebih dari 0 Kurang Dari 5 Lebih dari 8 kurang dari 11 : "))
rules1 = inputUser > 0
rules2 = inputUser < 5
rules3 = inputUser > 8
rules4 = inputUser < 11

jawaban1 = rules1 and rules2 or rules3 and rules4
print("jawabannya adalah :", jawaban1) 


