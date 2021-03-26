print ("=============================================")
print ("Soal 4 Tugas 4")
print ("=============================================")

x = int(input("Berapa usia kamu :"))
y = input("Apakah sudah lulus ujian kualifikasi (Y/T):").upper()

if x >= 18 and y == "Y":
    print("Kamu dapat mendaftar di kursus")
else:
    print("Kamu tidak dapat mendaftar di kursus")