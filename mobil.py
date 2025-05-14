class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def nyalakan(self):
        print(f"Mobil {self.merk} berwarna {self.warna} sedang dinyalakan.")

# Membuat objek
car = Mobil("Toyota", "Merah")
car.nyalakan()
