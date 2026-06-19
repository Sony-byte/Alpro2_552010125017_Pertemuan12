import csv
import os

FILE_PLAYSTATION = "playstation.csv"
FILE_PELANGGAN = "pelanggan.csv"
FILE_TRANSAKSI = "transaksi.csv"

playstation = []
pelanggan = []
transaksi = []

# DETEKSI DELIMITER CSV

def get_delimiter(path_csv):
    """
    Mendeteksi apakah file CSV menggunakan
    koma (,) atau titik koma (;).
    """

    with open(path_csv, "r", encoding="utf-8") as file:

        sample = file.read(1024)

        file.seek(0)

        try:
            dialect = csv.Sniffer().sniff(
                sample,
                delimiters=";,"
            )

            return dialect.delimiter

        except csv.Error:

            return ","

# LOAD DATA

def load_playstation():

    # Membaca data PlayStation dari file CSV.
    playstation.clear()

    if os.path.exists(FILE_PLAYSTATION):

        delimiter = get_delimiter(FILE_PLAYSTATION)

        with open(FILE_PLAYSTATION,
                  "r",
                  newline="",
                  encoding="utf-8") as file:

            reader = csv.DictReader(
                file,
                delimiter=delimiter
            )

            for row in reader:
                playstation.append(row)

def load_pelanggan():

    # Membaca data pelanggan dari file CSV.
    pelanggan.clear()

    if os.path.exists(FILE_PELANGGAN):

        delimiter = get_delimiter(FILE_PELANGGAN)

        with open(FILE_PELANGGAN,
                  "r",
                  newline="",
                  encoding="utf-8") as file:

            reader = csv.DictReader(
                file,
                delimiter=delimiter
            )

            for row in reader:
                pelanggan.append(row)

def load_transaksi():

    # Membaca data transaksi dari file CSV.
    transaksi.clear()

    if os.path.exists(FILE_TRANSAKSI):

        delimiter = get_delimiter(FILE_TRANSAKSI)

        with open(FILE_TRANSAKSI,
                  "r",
                  newline="",
                  encoding="utf-8") as file:

            reader = csv.DictReader(
                file,
                delimiter=delimiter
            )

            for row in reader:
                transaksi.append(row)

# SAVE DATA

def save_playstation():

    # Menyimpan data PlayStation ke file CSV (;)

    with open(FILE_PLAYSTATION,
              "w",
              newline="",
              encoding="utf-8") as file:

        field = ["id", "tipe", "status"]

        writer = csv.DictWriter(
            file,
            fieldnames=field,
            delimiter=";"
        )

        writer.writeheader()
        writer.writerows(playstation)

def save_pelanggan():

    # Menyimpan data pelanggan ke file CSV (;)
    with open(FILE_PELANGGAN,
              "w",
              newline="",
              encoding="utf-8") as file:

        field = ["id", "nama", "telepon"]

        writer = csv.DictWriter(
            file,
            fieldnames=field,
            delimiter=";"
        )

        writer.writeheader()
        writer.writerows(pelanggan)

def save_transaksi():

    # Menyimpan data transaksi ke file CSV (;)
    with open(FILE_TRANSAKSI,
              "w",
              newline="",
              encoding="utf-8") as file:

        field = ["pelanggan", "ps", "status"]

        writer = csv.DictWriter(
            file,
            fieldnames=field,
            delimiter=";"
        )

        writer.writeheader()
        writer.writerows(transaksi)

# CRUD PELANGGAN

def tambah_pelanggan():

    idp = input("ID Pelanggan : ")
    nama = input("Nama : ")
    telp = input("Telepon : ")

    pelanggan.append({
        "id": idp,
        "nama": nama,
        "telepon": telp
    })

    save_pelanggan()

    print("Data berhasil ditambahkan.")

def tampil_pelanggan():

    print("\n===== DATA PELANGGAN =====")

    if len(pelanggan) == 0:
        print("Belum ada data.")
        return

    for p in pelanggan:
        print(p["id"], "|", p["nama"], "|", p["telepon"])

def ubah_pelanggan():

    idp = input("Masukkan ID : ")

    for p in pelanggan:

        if p["id"] == idp:

            p["nama"] = input("Nama Baru : ")
            p["telepon"] = input("Telepon Baru : ")

            save_pelanggan()

            print("Data berhasil diubah.")
            return

    print("Data tidak ditemukan.")

def hapus_pelanggan():

    idp = input("Masukkan ID : ")

    for p in pelanggan:

        if p["id"] == idp:

            pelanggan.remove(p)

            save_pelanggan()

            print("Data berhasil dihapus.")
            return

    print("Data tidak ditemukan.")

# PLAYSTATION

def tampil_playstation():

    print("\n===== DATA PLAYSTATION =====")

    for ps in playstation:
        print(ps["id"], "|", ps["tipe"], "|", ps["status"])

# SEARCH

def cari_data():

    kata = input("Masukkan Kata Kunci : ").lower()

    ditemukan = False

    for p in pelanggan:

        if kata in p["nama"].lower():

            print("\nData Pelanggan")
            print(p)

            ditemukan = True

    for ps in playstation:

        if kata in ps["id"].lower() or kata in ps["tipe"].lower():

            print("\nData PlayStation")
            print(ps)

            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.")

# PENYEWAAN

def sewa_playstation():

    id_pelanggan = input("ID Pelanggan : ")
    id_ps = input("ID PlayStation : ")

    for ps in playstation:

        if ps["id"] == id_ps:

            if ps["status"] == "Disewa":

                print("PlayStation sedang disewa.")
                return

            ps["status"] = "Disewa"

            transaksi.append({

                "pelanggan": id_pelanggan,
                "ps": id_ps,
                "status": "Disewa"

            })

            save_playstation()
            save_transaksi()

            print("Penyewaan berhasil.")

            return

    print("PlayStation tidak ditemukan.")

# PENGEMBALIAN

def kembalikan_playstation():

    id_ps = input("ID PlayStation : ")

    for ps in playstation:

        if ps["id"] == id_ps:

            ps["status"] = "Tersedia"

            transaksi.append({

                "pelanggan": "-",
                "ps": id_ps,
                "status": "Dikembalikan"

            })

            save_playstation()
            save_transaksi()

            print("Pengembalian berhasil.")

            return

    print("PlayStation tidak ditemukan.")

# LAPORAN

def laporan():

    print("\n===== LAPORAN TRANSAKSI =====")

    if len(transaksi) == 0:

        print("Belum ada transaksi.")
        return

    for t in transaksi:

        print(
            t["pelanggan"],
            "|",
            t["ps"],
            "|",
            t["status"]
        )

# MENU

def menu():

    load_playstation()
    load_pelanggan()
    load_transaksi()

    while True:

        print("""
=====================================
   APLIKASI RENTAL PLAYSTATION
=====================================

1. Tambah Pelanggan
2. Tampilkan Pelanggan
3. Ubah Pelanggan
4. Hapus Pelanggan
5. Tampilkan PlayStation
6. Cari Data
7. Penyewaan
8. Pengembalian
9. Laporan Transaksi
0. Keluar

=====================================
""")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tambah_pelanggan()

        elif pilih == "2":
            tampil_pelanggan()

        elif pilih == "3":
            ubah_pelanggan()

        elif pilih == "4":
            hapus_pelanggan()

        elif pilih == "5":
            tampil_playstation()

        elif pilih == "6":
            cari_data()

        elif pilih == "7":
            sewa_playstation()

        elif pilih == "8":
            kembalikan_playstation()

        elif pilih == "9":
            laporan()

        elif pilih == "0":
            print("Program selesai.")
            break

        else:
            print("Menu tidak tersedia.")

menu()