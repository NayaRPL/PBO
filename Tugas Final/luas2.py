class Luas:
    def __init__(self) :
        self.persegi()
        self.segitiga()
        self.Lingkaran()
    class persegi:
        def __init__(self):
         self.sisi = 4
         
        def hitungLuas(self):
            return self.sisi*self.sisi
        # create 2 st inner class 
    class segitiga :
        def __init__(self):
            self.alas = 3
            self.tinggi =4
        def hitungLuas(self):
            return ((self.alas*self.tinggi)/2)
        
        # create 2 st inner class 
    class Lingkaran :
        def __init__(self):
            self.jari_jari=4.5
        def hitungLuas(self):
            return (3.14*(self.jari_jari*self.jari_jari))
                
outer = Luas()
objek1=outer.persegi()
objek2=outer.segitiga()
objek3=outer.Lingkaran()
print("luas dari persegi ",objek1.hitungLuas())
print("luas dari segitiga ",objek2.hitungLuas())
print("luas dari lingkaran ",objek3.hitungLuas())

# d1=outer.persegi(3)
# print("luas adalah ",d1.hitungLuas())

            
             
         
         
            
    