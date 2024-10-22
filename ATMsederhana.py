data_pengguna = {
    "234567": {"pin": 1432, "saldo": 1000000},
    "998899": {"pin": 4567, "saldo": 500000},
    "237788": {"pin": 5543, "saldo": 450000},
}

# Fungsi untuk mengecek saldo berdasarkan data pengguna atm
def cek_saldo(nomor_rekening):
    if nomor_rekening in data_pengguna:
        print("Saldo Anda:", data_pengguna[nomor_rekening]["saldo"])
    else:
      print(" Nomor Rekening Tidak Ditemukan.")

def tarik_tunai(nomor_rekening, jumlah):
    if nomor_rekening in data_pengguna:
        if data_pengguna[nomor_rekening]["saldo"] >= jumlah:
            data_pengguna[nomor_rekening]["saldo"] -= jumlah
            print(" Penarikan Berhasil. Saldo Anda Sekarang:", data_pengguna[nomor_rekening]["saldo"])
        else:
            print(" Saldo Tidak Mencukupi.")
    else:
     print(" Nomor Rekening Tidak Ditemukan.")

     def transfer(nomor_rekening_pengirim, nomor_rekening_tujuan, jumlah):
        if nomor_rekening_pengirim in data_pengguna and nomor_rekening_tujuan in data_pengguna:
           if data_pengguna[nomor_rekening_pengirim]["saldo"] >= jumlah:
              data_pengguna[nomor_rekening_pengirim]["saldo"] -= jumlah
              data_pengguna[nomor_rekening_tujuan]["saldo"] += jumlah
              print(" Transfer Berhasil.")
           else:
              print(" Saldo Tidak Mencukupi.")
        else:
           print(" Nomor Rekening Tidak Ditemukan.")

           # Program utama dalam program sederhana ini
           while True:
              print("\n======================================")
              print("|  Selamat Datang Di Atm Sederhana   |")
              print("|====================================| \n")
              nomor_rekening = input(" Masukkan Nomor Rekening: ")
              pin = int(input(" Masukkan PIN: "))
              if nomor_rekening in data_pengguna and data_pengguna[nomor_rekening]["pin"] == pin:
                 
                 while True:
                    print("\n===================================|")
                    print("|  Selamat Datang Di Atm Sederhana   |")
                    print("|====================================|")
                    print("|          1). Cek Saldo             |")
                    print("|          2). Transfer Uang         |")
                    print("|          3). Tarik Tunai           |")
                    print("|          4). Keluar                |")
                    print("|====================================|")
                    pilihan = input(" Pilih Menu (1/2/3/4): ")

                    if pilihan == "1":
                       cek_saldo(nomor_rekening)
                    elif pilihan == "2":
                       nomor_rekening_tujuan = input(" Masukkan Nomor Rekening Tujuan: ")
                       jumlah = int(input(" Masukkan Jumlah Yang Ingin Ditransfer: "))
                       transfer(nomor_rekening, nomor_rekening_tujuan, jumlah)
                    elif pilihan == "3":
                       jumlah = int(input(" Masukkan Jumlah Yang Ingin Ditarik: "))
                       tarik_tunai(nomor_rekening, jumlah)
                    elif pilihan == "4":
                       print(" Terima kasih Telah Menggunakan ATM Kami!")
                       break
                    else:
                       print(" Pilihan Tidak Valid!")
                 else:
                  print(" Nomor Rekening Atau PIN Salah!")