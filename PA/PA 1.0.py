import os
import time

#color
class color:
    g = '\033[92m'
    y = '\033[93m'
    r = '\033[91m'
    w = '\033[0m'
    b = '\033[34m'

users = {"user1" : "111"} #Sebagai database user yang telah terdaftar
admins = {"admin" : "admin"} #Sebagai database admin
reservasi = {"Meja 1" : "", "Meja 2" : "", "Meja 3" : "", "Meja 4" : "", "Meja 5" : "" }
menu = {"makanan" : ["Pizza", "Burger", "Spaghetti"], 
        "minuman" : ["Es Teh", "Kopi Susu", "Orange Juice"]} 
harga = {"harga_makanan" : [60000, 35000, 40000], 
         "harga_minuman" : [8000, 12000, 13000]}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def cekreservasi_admin():
    print(color.b+"="*60)
    print(color.g+"                      LIST RESERVASI")
    print(color.b+"="*60)
    for key, value in reservasi.items():
        print (color.g+(f" {key} : {value}"))
    print(color.b+"="*60)
    

def register():
    print(color.b+"="*60)
    print(color.g+"                Silahkan Registrasi Akun anda")
    print(color.b+"="*60)
    username = str(input(color.g+"\nMasukkan username: "+color.y))
    while username in users or username in admins:
        print(color.r+"="*60)
        print("              Maaf, username telah digunakan")
        print(color.r+"="*60)
        username = str(input(color.g+"Masukkan username: "+color.y))
    password = str(input(color.g+"Masukkan password: "+color.y))
    users[username] = password
    clear_screen()
    print(color.b+"="*60)
    print(color.g+"           Selamat, Akun anda berhasil terdaftar")
    print(color.b+"="*60)
    input(color.g+"\n          Tekan Enter untuk kembali ke menu utama")
    clear_screen()
    print(color.w+"kembali...")
    time.sleep(2)
    clear_screen()

def login():
    salah = 0
    print(color.b+"="*60)
    print(color.g+"                      Silahkan Login")
    print(color.b+"="*60)
    while True:
        username = str(input (color.g+"\n    Masukkan username: "+color.y))
        password = str(input(color.g+"    Masukkan password: "+color.y))
        if username in users.keys() and users[username] == password:
            clear_screen()
            print(color.w+"checking...")
            time.sleep(2)
            clear_screen()
            print(color.b+"="*60)
            print(color.g+"                      Login Berhasil")
            print(color.b+"="*60)
            input(color.g+"\n          Tekan Enter untuk masuk ke menu user")
            clear_screen()
            print(color.w+"Memasuki menu user...")
            time.sleep(2)
            clear_screen()
            usermenu()
        elif username in admins and admins[username] == password:
            clear_screen()
            print(color.w+"checking...")
            time.sleep(2)
            clear_screen()
            print(color.b+"="*60)
            print(color.g+"      LOGIN BERHASIL! (anda telah login sebagai ADMIN)")
            print(color.b+"="*60)
            time.sleep(2)
            input(color.g+"\n          Tekan Enter untuk masuk ke menu ADMIN")
            clear_screen()
            print(color.w+"Memasuki menu ADMIN...")
            time.sleep(2)
            clear_screen()
            adminmenu()
        else:
            clear_screen()
            print(color.w+"checking...")
            time.sleep(2)
            clear_screen()
            print(color.r+"="*60)
            print("""         LOGIN GAGAL! Username atau password salah
                    Silahkan coba lagi""")
            print(color.r+"="*60)
            salah +=1
        if salah == 3:
            print(color.r+"="*60)
            print("                 Anda sudah 3x gagal login")
            print(color.r+"="*60)
            time.sleep(2)
            input(color.g+"Tekan Enter untuk kembali ke menu utama")
            clear_screen()
            print(color.w+"Kembali ke menu utama...")
            time.sleep(2)
            clear_screen()
            mainmenu()

def mainmenu():
    while True:
        print(color.b+"="*60)
        print(color.g+"                         MAIN MENU")
        print(color.b+"="*60)
        print(color.g+"    [1] Register")
        print("    [2] Login")
        print("    [3] Exit")
        print(color.b+"="*60)
        pilihan = str(input(color.g+"Pilih Menu : "+color.y))
        if pilihan == "1":
            clear_screen()
            register()
        elif pilihan == "2":
            clear_screen()
            login()
        elif pilihan == "3":
            print(color.b+"="*60)
            print(color.g+"          Anda keluar dari program!, Terimakasih")
            print(color.b+"="*60)
            exit()
        else:
            print(color.r+"="*60)
            print("                    ERROR! Input Invalid")
            print("="*60)
            print(color.w+"\nLoading...")
            time.sleep(3)
            clear_screen()

def cekmenu():
    print(color.b+"="*60)
    print(color.g+"                        MENU Z'RESTO")
    print(color.b+"="*60)
    for kategori, items in menu.items():
        print(color.y+(f"    List {kategori}:".upper()))
        for i, item in enumerate(items, 1):
            harga_item = harga[f'harga_{kategori}'][i - 1]
            print(color.g+(f"\n    {i}. {item} : {harga_item}".upper()))
    print(color.b+"="*60)

def tambah_menu():
    print(color.b+"="*60)
    print(color.g+"                        TAMBAH MENU")
    print(color.b+"="*60)
    while True:
        tambahapa = str(input(color.g+"\nTambah Menu [makanan/minuman]: "+color.y)).lower()
        if tambahapa != "makanan" and tambahapa != "minuman":
            clear_screen()
            print(color.r+"="*60)
            print("                    Input tidak valid")
            print(color.r+"="*60)
            input("Tekan Enter untuk kembali ke Tambah Menu")
            clear_screen()
            tambah_menu()
        tambah = input(color.g+(f"Masukkan nama {tambahapa}: "+color.y))
        while True:
            try:
                harga_menu = int(input(color.g+"Masukkan harga: "+color.y))
                if harga_menu <= 0:
                    print(color.r+"="*60)
                    print("   Error! Harga tidak boleh = 0 atau bernilai negatif!")
                    print(color.r+"="*60)
                    continue
                else: 
                    menu[tambahapa].append(tambah)
                    harga[f'harga_{tambahapa}'].append(harga_menu)
                    print(color.g+(f"Berhasil menambahkan {tambah} seharga {harga_menu} ke dalam MENU"))
                    ulang = str(input(color.g+"\nApakah anda masih ingin menambah menu? [ya/tidak]: "+color.y)).lower()
                    while ulang not in ["ya", "tidak"]:
                        print(color.r+"\nInput tidak sesuai")
                        ulang = str(input(color.g+"\nApakah anda masih ingin menambah menu? [ya/tidak]: "+color.y)).lower()
                    if ulang == "ya":
                        clear_screen()
                        break
                    else:
                        clear_screen()
                        print(color.w+"Kembali ke menu ADMIN...")
                        time.sleep(2)
                        clear_screen()
                        adminmenu()
            except ValueError:
                print(color.r+"="*60)
                print("              Error! Inputan harus berupa angka")
                print(color.r+"="*60)
                continue
        
def hapus_menu():
    print(color.b+"="*60)
    print(color.g+"                        HAPUS MENU")
    print(color.b+"="*60)
    while True:
        hapusapa = str(input(color.g+"\nHapus Menu [makanan/minuman]: "+color.y)).lower()
        if hapusapa != "makanan" and hapusapa != "minuman":
            clear_screen()
            print(color.r+"="*60)
            print(color.r+"                    EROR! Input Invalid")
            print(color.r+"="*60)
            time.sleep(2)
            input(color.g+"          Tekan Enter untuk kembali ke Hapus Menu")
            clear_screen()
            hapus_menu()
        while True:
            try:
                cek_jenismenu(hapusapa)
                hapus = int(input(color.g+(f"\nMasukkan kode {hapusapa} yang ingin dihapus: "+color.y)))
                if hapus > len(menu[hapusapa]) or hapus <= 0:
                    clear_screen()
                    print(color.r+"="*60)
                    print(color.r+"                    EROR! Input Invalid")
                    print(color.r+"="*60)
                    time.sleep(2)
                    clear_screen()
                    continue
                else:
                    hapus = menu[hapusapa].pop(hapus-1)
                    print(color.g+(f"\nBerhasil menghapus {hapus} dari MENU"))
                    ulang = str(input(color.g+"\nApakah anda masih ingin menghapus menu? [ya/tidak]: "+color.y)).lower()
                    while ulang not in ["ya", "tidak"]:
                        clear_screen()
                        print(color.r+"="*60)
                        print(color.r+"                    EROR! Input Invalid")
                        print(color.r+"="*60)
                        time.sleep(2)
                        clear_screen()
                        ulang = str(input(color.g+"\nApakah anda masih ingin menghapus menu? [ya/tidak]: "+color.y)).lower()
                    if ulang == "ya":
                        clear_screen()
                        cekmenu()
                        break
                    else:
                        clear_screen()
                        print(color.w+"Kembali ke menu ADMIN...")
                        time.sleep(2)
                        clear_screen()
                        adminmenu()
            except ValueError:
                clear_screen()
                print(color.r+"="*60)
                print(color.r+"               EROR! Input harus berupa angka")
                print(color.r+"="*60)
                time.sleep(2)
                input(color.g+"                 Tekan Enter untuk kembali")
                clear_screen()
                continue

def ubah_harga():
    print(color.b+"="*60)
    print(color.g+"                      UBAH HARGA MENU")
    print(color.b+"="*60)   
    while True:
        ubahapa = str(input (color.g+"\nUbah Harga Menu [makanan/minuman]: "+color.y)).lower()
        if ubahapa != "makanan" and ubahapa != "minuman":
            clear_screen()
            print(color.r+"="*60)
            print(color.r+"                    EROR! Input Invalid")
            print(color.r+"="*60)
            time.sleep(2)
            clear_screen()
            ubah_harga()
        while True:
            try:
                cek_jenismenu(ubahapa)
                ubah_menu = int(input(color.g+(f"Masukkan kode {ubahapa} yang ingin diubah harganya: "+color.y)))
                if ubah_menu > len(menu[ubahapa]) or ubah_menu <= 0:
                    print(color.r+"="*60)
                    print("                  EROR! Kode tidak valid")
                    print(color.g+"             Silahkan masukkan kode yang valid")
                    print(color.r+"="*60)
                    continue
                else:
                    while True:
                        try:
                            hargabaru = int(input(color.g+("Masukkan harga baru: "+color.y)))
                            if hargabaru <= 0:
                                print(color.r+"="*60)
                                print("   Error! Harga tidak boleh = 0 atau bernilai negatif!")
                                print(color.r+"="*60)
                                continue
                            else:
                                clear_screen()
                                harga[f"harga_{ubahapa}"][ubah_menu-1] = hargabaru
                                print(color.g+(f"Berhasil mengubah harga {menu[ubahapa][ubah_menu-1]} menjadi {hargabaru}"))
                                time.sleep(2)
                                ulang = str(input(color.g+"\nApakah anda masih ingin mengubah harga menu? [ya/tidak]: "+color.y)).lower()
                                while ulang not in ["ya", "tidak"]:
                                    clear_screen()
                                    print(color.r+"="*60)
                                    print(color.r+"                    EROR! Input Invalid")
                                    print(color.r+"="*60)
                                    time.sleep(2)
                                    clear_screen()
                                    ulang = str(input(color.g+"\nApakah anda masih ingin mengubah harga menu? [ya/tidak]: "+color.y)).lower()
                                if ulang == "ya":
                                    clear_screen()
                                    break
                                else:
                                    clear_screen()
                                    print(color.w+"Kembali ke menu ADMIN...")
                                    time.sleep(2)
                                    clear_screen()
                                    adminmenu()
                        except ValueError:
                            clear_screen()
                            print(color.r+"="*60)
                            print(color.r+"               EROR! Input harus berupa angka")
                            print(color.r+"="*60)
                            time.sleep(2)
                            input(color.g+"                 Tekan Enter untuk kembali")
                            clear_screen()
                            continue
                if ulang == "ya":
                    clear_screen()
                    break
            except ValueError:
                clear_screen()
                print(color.r+"="*60)
                print(color.r+"               EROR! Input harus berupa angka")
                print(color.r+"="*60)
                time.sleep(2)
                input(color.g+"                 Tekan Enter untuk kembali")
                clear_screen()
                continue

def tambah_meja():
    print(color.b+"="*60)
    print(color.g+"                         TAMBAH MEJA")
    print(color.b+"="*60)          
    while True:
        try:
            cekreservasi_admin()
            nomor_tambah = int(input(color.g+"Masukkan nomor meja baru: "+color.y))
            if nomor_tambah <= 0:
                print(color.r+"="*60)
                print("  Error! Nomor Meja tidak boleh = 0 atau bernilai negatif!")
                print(color.r+"="*60)
                continue
            elif (f"Meja {nomor_tambah}") in list(reservasi.keys()):
                print(color.r+"="*60)
                print("             Error! Nomor Meja Sudah Tersedia")
                print(color.r+"="*60)
                continue
            reservasi[f"Meja {nomor_tambah}"] = ""
            print(color.g+(f"\nBerhasil Menambahkan Meja {nomor_tambah} ke List Reservasi Meja"))
            while True:
                ulang = str(input(color.g+"\nApakah anda masih ingin menambah meja? [ya/tidak]: "+color.y)).lower()
                if ulang == "ya":
                    clear_screen()
                    break
                elif ulang == "tidak":
                    clear_screen()
                    print(color.w+"Kembali ke menu ADMIN...")
                    time.sleep(2)
                    clear_screen()
                    adminmenu()
                else:
                    clear_screen()
                    print(color.r+"="*60)
                    print(color.r+"                    EROR! Input Invalid")
                    print(color.r+"="*60)
                    time.sleep(2)
                    clear_screen()
        except ValueError:
            clear_screen()
            print(color.r+"="*60)
            print(color.r+"               EROR! Input harus berupa angka")
            print(color.r+"="*60)
            time.sleep(2)
            input(color.g+"                 Tekan Enter untuk kembali")
            clear_screen()
            continue

def hapus_meja():
    print(color.b+"="*60)
    print(color.g+"                         HAPUS MEJA")
    print(color.b+"="*60) 
    while True:
        try:
            cekreservasi_admin()
            nomor_hapus = int(input(color.g+"Masukkan nomor meja yang ingin dihapus: "+color.y))
            if (f"Meja {nomor_hapus}") not in list(reservasi.keys()):
                clear_screen()
                print(color.r+"="*60)
                print("                Error! Nomor Meja Tidak ada")
                print(color.r+"="*60)
                time.sleep(2)
                clear_screen()
                continue
            else:
                del(reservasi[f"Meja {nomor_hapus}"])
                print(color.g+(f"\nBerhasil Menghapus Meja {nomor_hapus} dari List Reservasi Meja"))
                while True:
                    ulang = str(input(color.g+"\nApakah anda masih ingin menghapus meja? [ya/tidak] : "+color.y)).lower()
                    if ulang == "ya":
                        clear_screen()
                        hapus_meja()
                    elif ulang == "tidak":
                        clear_screen()
                        print(color.w+"Kembali ke menu ADMIN...")
                        time.sleep(2)
                        clear_screen()
                        adminmenu()
                    else:
                        clear_screen()
                        print(color.r+"="*60)
                        print(color.r+"                    EROR! Input Invalid")
                        print(color.r+"="*60)
                        time.sleep(2)
                        clear_screen()
        except ValueError:
            clear_screen()
            print(color.r+"="*60)
            print(color.r+"               EROR! Input harus berupa angka")
            print(color.r+"="*60)
            time.sleep(2)
            input(color.g+"                 Tekan Enter untuk kembali")
            clear_screen()
            continue

def ubah_reservasi():
    print(color.b+"="*60)
    print(color.g+"                      UBAH RESERVASI")
    print(color.b+"="*60)
    while True:
        try:
            cekreservasi_admin()
            nomor_ubah = int(input(color.g+"Masukkan Nomor Meja Yang Ingin Diubah Datanya: "+color.y))
            if (f"Meja {nomor_ubah}") not in list(reservasi.keys()):
                clear_screen()
                print(color.r+"="*60)
                print("                Error! Nomor Meja Tidak ada")
                print(color.r+"="*60)
                time.sleep(2)
                clear_screen()
                continue
            else:
                ubah_data = str(input(color.g+"Masukkan Perubahan Data (Tekan Enter untuk Menghapus Nama Pereservasi): "+color.y))
                reservasi[f"Meja {nomor_ubah}"] = ubah_data
                print(color.g+(f"\nBerhasil mengubah data {f'Meja {nomor_ubah}'}\033[0m"))
                while True:
                    ulang = str(input(color.g+"\nApakah anda masih ingin mengubah data reservasi? [ya/tidak]: "+color.y)).lower()
                    if ulang == "ya":
                        clear_screen()
                        ubah_reservasi()
                    elif ulang == "tidak":
                        clear_screen()
                        print(color.w+"Kembali ke menu ADMIN...")
                        time.sleep(2)
                        clear_screen()
                        adminmenu()
                    else:
                        clear_screen()
                        print(color.r+"="*60)
                        print(color.r+"                    EROR! Input Invalid")
                        print(color.r+"="*60)
                        time.sleep(2)
                        clear_screen()
        except ValueError:
            clear_screen()
            print(color.r+"="*60)
            print(color.r+"               EROR! Input harus berupa angka")
            print(color.r+"="*60)
            time.sleep(2)
            input(color.g+"                 Tekan Enter untuk kembali")
            clear_screen()
            continue

def adminmenu():
    while True:
        print(color.b+"="*60)
        print(color.g+"                         ADMIN MENU")
        print(color.b+"="*60)
        print(color.g+"    [1] Tampilkan Menu")
        print("    [2] Tambah Menu")
        print("    [3] Hapus Menu")
        print("    [4] Ubah Harga Menu")
        print("    [5] Tampilkan List Reservasi")
        print("    [6] Tambah Meja Reservasi")
        print("    [7] Hapus Meja Reservasi")
        print("    [8] Ubah Data Reservasi")
        print("    [9] Kembali ke Main Menu")
        print(color.b+"="*60)
        pilihan = str(input(color.g+"Masukkan Pilihan : "+color.y))
        if pilihan == "1":
            clear_screen()
            print(color.w+"Loading...")
            time.sleep(2)
            clear_screen()
            cekmenu()
        elif pilihan == "2":
            clear_screen()
            print(color.w+"Loading...")
            time.sleep(2)
            clear_screen()
            tambah_menu()
        elif pilihan == "3":
            clear_screen()
            print(color.w+"Loading...")
            time.sleep(2)
            clear_screen()
            cekmenu()
            hapus_menu()
        elif pilihan == "4":
            clear_screen()
            print(color.w+"Loading...")
            time.sleep(2)
            clear_screen()
            cekmenu()
            ubah_harga()
        elif pilihan == "5":
            clear_screen()
            print(color.w+"Loading...")
            time.sleep(2)
            clear_screen()
            cekreservasi_admin()
        elif pilihan == "6":
            clear_screen()
            print(color.w+"Loading...")
            time.sleep(2)
            clear_screen()
            tambah_meja()
        elif pilihan == "7":
            clear_screen()
            print(color.w+"Loading...")
            time.sleep(2)
            clear_screen()
            hapus_meja()
        elif pilihan == "8":
            clear_screen()
            print(color.w+"Loading...")
            time.sleep(2)
            clear_screen()
            cekreservasi_admin()
            ubah_reservasi()
        elif pilihan == "9":
            clear_screen()
            print(color.w+"\nMengembalikan ke menu utama...")
            time.sleep(2)
            clear_screen()   
            mainmenu()
        else:
            clear_screen()
            print(color.r+"="*60)
            print("                  Error! Pilihan tidak ada")
            print(color.r+"="*60)
            input("\n                 Tekan Enter untuk kembali")
            clear_screen()
            
def cek_jenismenu(jenis_pesanan):
    if jenis_pesanan == "makanan":
        print(color.b+"="*60)
        print(color.y+"                        LIST MAKANAN")
        print(color.b+"="*60)
        for i in range(len(menu["makanan"])):
            print(color.g+(f"    {i + 1}. {menu['makanan'][i]} : {harga['harga_makanan'][i]}".upper()))        
    elif jenis_pesanan == "minuman":
        print(color.b+"="*60)
        print(color.y+"                        LIST MINUMAN")
        print(color.b+"="*60)     
        for i in range(len(menu["minuman"])):
            print(color.g+(f"    {i + 1}. {menu['minuman'][i]} : {harga['harga_minuman'][i]}".upper()))      

def pesan_makanan_minuman():
    global total_harga, pesanan
    pesanan = []
    total_harga = 0
    while True:
        jenis_pesanan = str(input(color.g+"\nApa yang ingin Anda pesan [makanan/minuman/selesai]? "+color.y)).lower()
        if jenis_pesanan == "selesai":
            break
        elif jenis_pesanan not in ["makanan", "minuman"]:
            print(color.r+"="*60)
            print("                    Pilihan tidak valid")
            print("     Silakan pilih 'makanan', 'minuman', atau 'selesai'")
            print(color.r+"="*60)
        else:
            cek_jenismenu(jenis_pesanan)
            while True:
                try:
                    kode = int(input(color.g+"\nMasukkan kode makanan/minuman yang ingin dipesan (0 untuk selesai): "+color.y))
                    if kode == 0:
                        break
                    elif kode > len(menu[f"{jenis_pesanan}"]) or kode < 0: 
                        print(color.r+"="*60)
                        print("                  EROR! Kode tidak valid")
                        print("             Silahkan masukkan kode yang valid")
                        print(color.r+"="*60)
                    else:
                        kode -= 1
                        jumlah = int(input(color.g+"\nJumlah: "+color.y))
                        item = menu[f"{jenis_pesanan}"][kode]
                        harga_item = harga[f'harga_{jenis_pesanan}'][kode]
                        pesanan.append((item, harga_item, jumlah))
                        total_harga += harga_item * jumlah
                        print(color.g+(f"{item} (x{jumlah}): ditambahkan ke pesanan."))
                except ValueError:
                    print(color.r+"="*60)
                    print("                  EROR! Kode tidak valid")
                    print("             Silahkan masukkan kode yang valid")
                    print(color.r+"="*60)
 
    if len(pesanan) > 0:
        struk()
        usermenu()
    else:
        print(color.r+"="*60)
        print(color.g+"             Anda belum memesan makanan apapun")
        print(color.r+"="*60)
        input(color.w+"\n                 Tekan Enter untuk memesan")
        clear_screen()
        pesan_makanan_minuman()

def struk():        
    print("="*50)
    print("||                                              ||")
    print("||                Struk Pesanan                 ||")
    print("||                                              ||")
    print("="*50)                               
    print(f"|| Nama pelanggan       : {nama}")
    print(f"|| Nomor meja reservasi : {nomor_reservasi}")
    for (item, harga_item, jumlah) in (pesanan):
        print(f"|| Pesanan              : {jumlah} {item} (Rp.{harga_item * jumlah})")
    print("-"*49)
    print(f"|| Total  harga         : Rp.{total_harga}")
    print(f"="*50)
        
def cekreservasi_user():
    print(color.b+"="*60)
    print(color.g+"                Silahkan reservasi meja anda")
    print("                  List meja yang tersedia")
    print(color.b+"="*60)
    for key, value in reservasi.items():
        if value == "":
            print (color.g+(f"    {key}")) 
    print(color.b+"="*60)
    
def reservasi_meja():
    global nama, nomor_reservasi
    while True:
        try:
            nomor_reservasi = int(input(color.g+"\nMasukkan Nomor Meja yang Ingin Direservasi: "+color.y))
            if (f"Meja {nomor_reservasi}") not in list(reservasi.keys()) or reservasi[(f"Meja {nomor_reservasi}")] != "":
                print(color.r+"="*60)
                print("              EROR! Nomor Meja Tidak Tersedia")
                print(color.r+"="*60)
                continue
            else:
                nama = str(input(color.g+"Silahkan masukkan nama Pereservasi: "+color.y))
                reservasi[f"Meja {nomor_reservasi}"] = nama
                clear_screen()
                print(color.b+"="*60)
                print(color.g+(f"          Berhasil Mereservasi Meja {nomor_reservasi} atas nama {nama}"))
                print(color.b+"="*60)
                break
        except ValueError:
            print(color.r+"="*60)
            print("""                           EROR!
                Inputan harus berupa angka""")
            print(color.r+"="*60)
            continue

def usermenu():
    while True:        
        print(color.b+"="*60)
        print(color.g+"                          USER MENU")
        print(color.b+"="*60)
        print(color.g+"    [1] Reservasi")
        print("    [2] Logout")
        print(color.b+"="*60)
        pilihan = str(input(color.g+"Masukkan Pilihan : "+color.y))
        if pilihan == "1":
            clear_screen()
            print(color.w+"Memasuki menu Reservasi...")
            time.sleep(2)
            clear_screen()
            cekreservasi_user()
            reservasi_meja()
            time.sleep(2)
            clear_screen()
            print(color.b+"="*60)
            print(color.g+"                      Silahkan Pesan")
            cekmenu()
            pesan_makanan_minuman()
            clear_screen()
            usermenu()
        if pilihan == "2":
            input(color.g+"\n          Tekan Enter untuk kembali ke menu utama")
            clear_screen()
            print(color.w+"Kembali ke menu utama...")
            time.sleep(2)
            clear_screen()
            mainmenu()
        else:
            clear_screen()
            print(color.r+"="*60)
            print("                     EROR! Input Invalid")
            print(color.r+"="*60)
            print(color.w+"\nLoading...")
            time.sleep(3)
            clear_screen()

clear_screen()
print(color.b+"="*60)
print(color.g+"""                     Selamat datang di
                          Z'Resto          """)

mainmenu()