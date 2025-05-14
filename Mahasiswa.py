class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def cetak_krs(self):
        print(f"Mahasiswa {self.nama} dengan NIM {self.nim} telah mencetak KRS.")

# Membuat objek
mhs = Mahasiswa("Arti", "2104411001")
mhs.cetak_krs()
