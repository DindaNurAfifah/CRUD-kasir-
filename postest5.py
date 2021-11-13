def login():
    print("==============MENU==============")
    print("[1] Pelanggan")
    print("[2] Admin")
    print("[3] Keluar")
    print("================================")

def pelanggan():
    print("==============MENU==============")
    print("[1] Show Menu")
    print("[2] Show Stock")
    print("[3] Kembali")
    print("================================")

def admin():
        print("==============MENU==============")
        print("[1] Show Data")
        print("[2] Insert Data")
        print("[3] Update Data")
        print("[4] Delete Data")
        print("[5] Kembali")
        print("================================")

def garis():
    print("=" * 40)

dict_Bunga = {"Inilah Menu yang Kami Mliki": "!",
        "Bunga Mawar Merah"      : 10000,
        "Bunga Mawar Pelangi"    : 20000,
        "Bunga Matahari"         : 16000,
        "Bunga Kapas"            : 18000,
        "Bunga Tulip"            : 12000,
        "Bunga Mawar Putih"      : 10000,
        "Bunga Lily"             : 15000,
        "Buka Daisy"             : 16000}

dict_Stok ={"Inilah Stock Bunga Kami": "!",
        "Bunga Mawar Merah"      : 200,
        "Bunga Mawar Pelangi"    : 230,
        "Bunga Matahari"         : 50,
        "Bunga Kapas"            : 75,
        "Bunga Tulip"            : 100,
        "Bunga Mawar Putih"      : 200,
        "Bunga Lily"             : 15000,
        "Buka Daisy"             : 16000}

#======================================================

login()
pilih = input("Pilih Menu:")

if pilih == "1" or pilih == "Pelanggan" :
    garis()
    print("Selamat Datang Di Toko Bunga HappyRoof!")
    print("Silahkan Memilih Menu")
    garis()
    pelanggan()
    pilih1 = input("Pilih Menu: ")
    garis()
    if pilih1 == "1" or pilih1 == "Show Menu":
        garis()
        for i,j in dict_Bunga.items():
            print("{} = {}".format(i, j))
        garis()
        input("Tekan [Enter] Untuk Kembali")
        pelanggan()
    elif pilih1 == "2" or pilih1 == "Show Stock":
        garis()
        for i,j in dict_Stok.items():
            print("{} = {}".format(i, j))
        garis()
        input("Tekan [Enter] Untuk Kembali")
        pelanggan()
    elif pilih1 == "3" or pilih1 == "Kembali":
        garis()
        print("Terimakasi Sudah Mengunjungi Menu Pelanggan!")
        print("Kembali Ke Menu Login...")
        input("Tekan [Enter] Untuk Kembali")
        garis()
        login()
    else:
        garis()
        print("Menu yang Anda Pilih Tidak Tersedia!")
        print("Kembali Ke Menu Pelanggan...")
        input("Tekan [Enter] Untuk Kembali")
        pelanggan()

elif pilih == "2" or pilih == "Admin":
    garis()
    print("Perlu Melakukan login")
    garis()
    username = input("Username: ")
    password = input("Password: ")
    garis()
    if username == "Dinda" or username == "dinda" and password == "061":
        print("Berhasil Login")
        print("Memasuki Menu Admin...")
        admin()
        pilih2 = input("Pilih Menu: ")
        if pilih2 == "1" or pilih2 == "Show Data":
            garis()
            for i,j in dict_Bunga.items():
                print("{} = {}".format(i, j))
            garis()
            input("Tekan [Enter] Untuk Kembali")
            admin()
        elif pilih2 == "2" or pilih2 == "Insert Data":
            garis()
            for i,j in dict_Bunga.items():
                print("{} = {}".format(i, j))
            garis()
            insert = input("Bunga yang Akan ditambah: ")
            price = int(input("Harga Bunga yang Ditambahkan: "))
            garis()
            dict_Bunga.update({insert: price})
            for i,j in dict_Bunga.items():
                print("{} = {}".format(i, j))
            garis()
            input("Tekan [Enter] Untuk Kembali")
            admin()
        elif pilih2 == "3" or pilih2 == "Update Data":
            garis()
            for i,j in dict_Bunga.items():
                print("{} = {}".format(i, j))
            garis()
            update = input("Pilih Bunga yang di edit: ")
            garis()
            del dict_Bunga[update]
            ganti_bunga = input("Masukan Nama Bunga Baru: ")
            ganti_harga = input("Masukan Harga Bunga Baru: ")
            garis()
            dict_Bunga[ganti_bunga] = ganti_harga
            for i,j in dict_Bunga.items():
                print("{} = {}".format(i, j))
            garis()
            input("Tekan [Enter] Untuk Kembali")
            admin()
        elif pilih2 == "4" or pilih2 == "Delete Data":
            garis()
            for i,j in dict_Bunga.items():
                print("{} = {}".format(i, j))
            garis()
            delete = input("Bunga yang Mau di Hapus: ")
            del dict_Bunga[delete]
            for i,j in dict_Bunga.items():
                print("{} = {}".format(i, j))
            garis()
            input("Tekan [Enter] Untuk Kembali")
            admin()
        elif pilih2 == "5" or pilih2 == "Kembali":
            garis()
            print("Terimakasih Telah Mengunjungi Menu Admin!")
            print("Kembali ke Menu login...")
            input("Tekan [Enter] Untuk Kembali")
            login()
        else:
            garis()
            print("Menu yang Anda Pilih Tidak Tersedia!")
            print("Kembali Ke Menu Admin...")
            input("Tekan [Enter] Untuk Kembali")
            admin()
    
elif pilih == "3" or pilih == "Keluar":
    garis()
    print("Terimakasih Telah Mengunjungi Sistem Kami!")
    garis()

else:
    garis()
    print("Menu yang Anda Pilih Tidak Tersedia!")
    print("Kembali Ke Menu Login...")
    input("Tekan [Enter] Untuk Kembali")
    login()
    
