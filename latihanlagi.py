# Variabel loop
ulang = 'y'

while ulang.lower() == 'y':

    # Input Identitas
    nama = input("Nama Anda: ")
    asal = input("Asal Kota: ")
    umur = input("Umur Anda:")

    print("####### HASIL IDENTITAS ANDA #######")

    print(f"Nama: {nama}")
    print(f"Asal: {asal}")
    print(f"Umur: {umur}")

    # Menanyakan apakah ingin melakukan perhitungan lagi
    ulang = input("Apakah Anda ingin melakukan perhitungan lagi? (y/t): ")

    print("Thanks You! Sampai jumpa.:)")