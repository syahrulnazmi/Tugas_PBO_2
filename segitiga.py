class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        luas = 0.5 * self.alas * self.tinggi
        print(f"Luas segitiga adalah {luas}")

# Membuat objek
sgt = Segitiga(10, 5)
sgt.hitung_luas()
