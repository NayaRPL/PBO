print('''  Menu Menghitung Luas 
      1.Persegi
      2.Lingkaran
      3.Segitiga''')
pilihan=int(input("masukkan pilihan : "))
if pilihan == 1:
    sisi = int(input("masukkan nilai sisi persegi : "))
    Luas_Persegi = sisi*sisi
    print("luas persegi adalah  ",Luas_Persegi)
elif pilihan == 2:
    pi=22/7
    jari_jari=int(input("masukkan jari jari lingkaran "))
    luas_lingkaran = pi*(jari_jari**2)
    print("luas lingkaran adalah ", luas_lingkaran)
elif pilihan ==3:
    alas  = int(input("masukkan nilai alas persegi : "))
    tinggi = int(input("masukkan nilai tinggi persegi : "))
    Luas_segitiga=1/2*alas*tinggi
    print(  " luas segigitga adalah ",Luas_segitiga)
else: 
    print("coba ulangi , pilihan anda tidak tedapat dalam menu")