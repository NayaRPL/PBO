import math
class BangunRuang:
    def luas(self):
        pass

    def volume(self):
        pass

    def printLuas(self):
        print( self.luas())

    def printVolume(self):
        print(self.volume())
        
    def info(self):
        print("Nama : Nurul Inayah")
        print("Kelas : Informatika G")
      

class Balok(BangunRuang):
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0

    def luas(self):
        luas = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi)
        return luas;

    def volume(self):
        volume  = self.panjang * self.lebar * self.tinggi
        return volume;
    
class Tabung(BangunRuang):
        def __init__(self):
            self.jari_jari = 0
            self.tinggi = 0
    
        def luas(self):
            l = 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)
            return round(l, 2)
 
        def volume(self):
            v = math.pi * (self.jari_jari ** 2) * self.tinggi
            return round(v, 2)

class Kubus(BangunRuang):
    def __init__(self):
        self.sisi = 0

    def luas(self):
        l = 6 * (self.sisi**2)
        return l

    def volume(self):
        v = self.sisi**3
        return v

def ulang():
    print("Ingin menghitung lagi? (y/n)")
    inp = input("=> ").lower()
    return True if inp == "y" else False 

#panggil class

kubus = Kubus()
balok = Balok()
tabung = Tabung()

while True:
    print("""\nPilih Bangun Ruang
1. Balok
2. Tabung
3. Kubus
4. Berhenti""")
    pilihan = input("=> ")

    if pilihan == "1":
        while True:
            print("""\n1. Luas
                       2. Volume
                       3. Keluar""")
            pilihan1 = input("=> ")
            
            if pilihan1 == "1":
                while True:
                    balok.panjang = float(input("Masukkan Panjang: "))
                    balok.lebar = float(input("Masukkan Lebar: "))
                    balok.tinggi = float(input("Masukkan Tinggi: "))
                    print("luas dari balok adalah : ")
                    balok.printLuas()
                    balok.info()

                    if ulang() != True:
                        break
            elif pilihan1 == "2":
                while True:
                    balok.panjang = float(input("Masukkan Panjang: "))
                    balok.lebar = float(input("Masukkan Lebar: "))
                    balok.tinggi = float(input("Masukkan Tinggi: "))
                    print("luas dari volume adalah : ")
                    balok.printVolume()
                    balok.info()
                    if ulang() != True:
                        break
            elif pilihan1 == "3":
                break
            else:
                    print("Masukkan pilihan yang Benar!")
                
                    
    if pilihan == "2":
        while True:
            print("""\n1. Luas
                       2. Volume
                       3. Keluar """)
            pilihan1 = input("=> ")
            
            if pilihan1 == "1":
                while True:
                    balok.jari_jari = float(input("Masukkan jari-jari: "))
                    balok.tinggi = float(input("Masukkan Tinggi: "))
                    print("luas dari luas adalah : ")
                    balok.printLuas()
                    balok.info()
                    if ulang() != True: 
                        break
            elif pilihan1 == "2":
                while True:
                    balok.panjang = float(input("Masukkan Panjang: "))
                    balok.tinggi = float(input("Masukkan Tinggi: "))
                    print("luas dari volume adalah : ")
                    balok.printVolume()
                    if ulang() != True:
                        break
            elif pilihan1 == "3":
                break
            else:
                    print("Masukkan pilihan yang Benar!")
    if pilihan == 3:
        while True:
            print("""\n1. Luas
                       2. Volume
                       3. Keluar """)
            pilihan1 = input("=> ")
            
            if pilihan1 == "1":
                while True:
                    kubus.sisi = float(input("Masukkan Sisi: "))
                    print("luas dari luas adalah : ")
                    balok.printLuas()
                    balok.info()
                    if ulang() != True:
                        break
            elif pilihan1 == "2":
                while True:
                    kubus.sisi = float(input("Masukkan Sisi: "))
                    balok.printVolume()
                    if ulang() != True:
                        break
            elif pilihan1 == "3":
                break
            else:
                    print("Masukkan pilihan yang Benar!")
print("Program berhenti. Selamat tinggal.")