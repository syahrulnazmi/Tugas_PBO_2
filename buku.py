class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info_buku(self):
        print(f"Buku berjudul '{self.judul}' ditulis oleh {self.penulis}.")

# Membuat objek
bk = Buku("Pemrograman Python", "Ari Wijaya")
bk.info_buku()
