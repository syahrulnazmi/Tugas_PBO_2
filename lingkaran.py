import math

class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        luas = math.pi * self.jari_jari ** 2
        print(f"Luas lingkaran dengan jari-jari {self.jari_jari} adalah {luas:.2f}")

# Membuat objek
blt = Lingkaran(7)
blt.hitung_luas()
