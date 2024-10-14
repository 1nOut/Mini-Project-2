from prettytable import PrettyTable

tabel = PrettyTable()

daftarbarang = {
    "Sword":  15,
    "Shield": 20,
    "Heal Potion": 5,
    "Mana Potion":5,
    "Bow": 15,
    "Arrow": 3,
}



def tabelnya():
    tabel.clear_rows() 
    tabel.title = "Item Shop"
    tabel.field_names = ["Nama", "Harga"]
    for nama, harga in daftarbarang.items():
        tabel.add_row([nama, f"{harga} G"])
    print(tabel)

inventory_pembeli = {}


def admin() :
    while(True) :
        try :
            tabel.clear_rows()
            tabel.title = "Menu Admin"
            tabel.field_names = ["No", "Pilihan"]
            tabel.add_row(["1", "Create"])
            tabel.add_row(["2", "Read"])
            tabel.add_row(["3", "Update"])
            tabel.add_row(["4", "Delete"])
            tabel.add_row(["5", "Keluar"])
            print(tabel)
            print("")

            pilihanadmin = int(input("Pilih menu: "))
            if pilihanadmin == 1 :
                nambahbarang = input("Masukkan nama barang: ")
                if nambahbarang in daftarbarang:
                    print("Barang sudah ada di dalam tabel")
                else:
                    harga = int(input("Masukkan harga: "))
                    if harga > 0:
                        daftarbarang[nambahbarang] = harga
                        print("Data sudah dimasukkan")
                    else:
                        print("Tidak bisa menambahkan harga dengan nilai dibawah 0")
            elif pilihanadmin == 2:
                print("")
                tabelnya()
                print("")
            elif pilihanadmin == 3:
                updatebarang = input("Masukkan nama barang: ")
                if updatebarang not in daftarbarang:
                    print("Maaf, barang tidak ada di dalam tabel")
                else:
                    harga = int(input("Masukkan harga: "))
                    if harga > 0:
                        daftarbarang.update({updatebarang: harga})
                        print(f"Harga barang {updatebarang} berhasil diubah") 
                    else:
                        print("Tidak bisa menambahkan harga dengan nilai dibawah 0")
            elif pilihanadmin == 4:
                hapus= input("Masukkan nama barang: ")
                if hapus in daftarbarang :
                    daftarbarang.pop(hapus)
                    print(f"Barang {hapus} berhasil dihapus")
                else:
                    print("Barang tidak ada di dalam tabel")
            elif pilihanadmin == 5:
                print("Selamat tinggal")
                print("")
                return True
            else:
                print("Tidak ada pilihan di dalam menu")
                print("")
                print("Silahkan coba lagi")
        except ValueError :
            print("Anda harus mengetik angka")

gold = 20
def pembeli() :
    global gold
    global inventory_pembeli
    while(True) :
        try :
            tabel.clear_rows()
            tabel.title = "Menu Pembeli"
            tabel.field_names = ["No", "Pilihan"]
            tabel.add_row(["1", "Tampilkan Barang"])
            tabel.add_row(["2", "Beli Barang"])
            tabel.add_row(["3", "Dompet"])
            tabel.add_row(["4", "Inventory"])
            tabel.add_row(["5", "Keluar"])
            print(tabel)
            print("")
            pilihanpembeli = int(input("Pilih menu: "))
            print("")
            if pilihanpembeli == 1 :
                tabelnya()
            elif pilihanpembeli == 2 :
                beli = input("Masukkan Nama Barang: ")
                if beli in daftarbarang:
                    hargabeli = daftarbarang[beli]
                    if hargabeli <= gold:
                        gold -= hargabeli
                        if beli in inventory_pembeli:
                            inventory_pembeli[beli] += 1
                        else:
                            inventory_pembeli[beli] = 1
                        print(f"Selamat barang {beli} berhasil dibeli !")
                        print(f"Sisa gold anda adalah {gold} G")
                    else:
                        print("Gold kurang, silahkan isi terlebih dahulu!")
                else:
                    print(f"Tidak ada barang dengan nama {beli}")
            elif pilihanpembeli == 3:
                    print("Pilihan: ")
                    print("1. Tampilkan jumlah Gold")
                    print("2. Isi Gold")
                    pilihandompet = int(input("Pilih menu: "))
                    if pilihandompet == 1:
                        print(f"Total Gold anda adalah {gold} G")
                    elif pilihandompet == 2 :
                        tambahgold = int(input("Masukkan jumlah Gold yang ingin diisi: "))
                        if tambahgold > 0:
                            gold += tambahgold
                            print(f"Gold anda sekarang adalah: {gold} G")
                        else:
                            print("Gold yang diisi tidak boleh kurang dari 0")
                    else:
                        print("Tidak ada pilihan menu dengan angka tersebut")
            elif pilihanpembeli == 4:
                print("Inventory Anda:")
                for barang, jumlah in inventory_pembeli.items():
                    print(f"{barang}: {jumlah} buah")
                print("")
            elif pilihanpembeli == 5:
                print("Terima kasih, silahkan datang kembali lagi !")
                return True
            else:
                print("Tidak ada pilihan di dalam menu")
                print("")
                print("Silahkan coba lagi")
        except ValueError :
            print("Anda harus mengetik angka")    


akunadmin = {
    "Admin" : 12345
}

akunpembeli = {
    "Adventurer" : 12345
}

        
while(True) :
    try :
        tabel = PrettyTable()
        tabel.title = "Menu Role"
        tabel.field_names = ["No", "Pilihan"]
        tabel.add_row(["1", "Admin"])
        tabel.add_row(["2", "Pembeli"])
        tabel.add_row(["3", "Keluar"])
        print(tabel)
        print("")
        pilihanrole = int(input("Masukkan pilihan: "))
        if pilihanrole == 1:
            username = input("Masukkan username: ")
            password = int(input("Masukkan password: "))
            if username in akunadmin and akunadmin[username] == password:
                print("Login berhasil!")
                print("Selamat datang Adventurer !")
                admin()
            else:
                print("Username atau password salah!")
        elif pilihanrole == 2:
            username = input("Masukkan username: ")
            password = int(input("Masukkan password: "))
            if username in akunpembeli and akunpembeli[username] == password:
                print("Login berhasil!")
                pembeli()
            else:
                print("Username atau password salah!")
        elif pilihanrole == 3:
            print("Terima kasih atas kunjungan Anda")
            break
        else:
            print("Tidak ada pilihan di dalam menu")
    except(ValueError):
        print("Anda harus mengetik angka")