# enkapsulasi dengan public access modifier

class pegawai:
    def __init__(self, nama, salary):
        self.nama=nama
        self.gaji=salary
        self.gaji_final= self.gaji - (0.2 * self.gaji)

obj1 = pegawai("Agus", 1000)
print(obj1.gaji_final)

obj1.gaji_final = 5000
print(f"Gaji final = {obj1.gaji_final}")