class luas:
    def __init__(self,sisi,alas,tinggi,jari) :
        self.sisi=sisi
        self.alas=alas
        self.tinggi=tinggi
        self.jari=jari
        
    def persegi(self):
            return self.sisi*self.sisi
    
    def segitiga(self):
      return ((self.alas*self.tinggi)/2)
  
    def lingkaran(self):
            return (3.14*(self.jari*self.jari))
        
objek1=luas(2,2,3,4)

print("ini merupkan luas persegi : ",objek1.persegi())
print("ini merupkan luas persegi : ",objek1.segitiga())
print("ini merupkan luas persegi : ",objek1.lingkaran())
        
        