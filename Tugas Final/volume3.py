class volume:
    def __init__(self,sisi,alas,tinggi,tinggiPrisma,jari_jari,tinggi_tabung) :
      self.sisi=sisi
      self.alas=alas
      self.tinggi=tinggi
      self.tinggiPrisma=tinggiPrisma
      self.tinggi_tabung=tinggi_tabung
      self.jari_jari=jari_jari
    
    def volumeKubus(self):
        return self.sisi**3
        
    def volumePrismaSegitiga(self):
        return (((self.alas*self.tinggi)/2)*self.tinggiPrisma)
    
    def volumeTabung(self):
        return (3.14*(self.jari_jari*self.jari_jari)*self.tinggi_tabung)

objek=volume(2,3,4,6,3,5)
print("volume dari kubus adalah : ",objek.volumeKubus())
print("volume dari prisma segitiga  adalah : ",objek.volumePrismaSegitiga())
print("volume dari tabung adalah : ",objek.volumeTabung())

    
           
             
    