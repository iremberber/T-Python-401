"""#Sınıf Tanımlama

class VeriBilimi():
    print("sınıf 1")
    

#Sınıf Özellikleri (Class Attributes)

class VeriBilimci():
    bolum = ''
    sql = 'evet'
    deneyim_yili = 0
    bildigi_diller = [] 

#Sınıfların özelliklerine erişmek

VeriBilimci.bolum

#Sınıfların özelliklerini değiştirmek

VeriBilimci.sql = "hayır"

VeriBilimci.sql

#Sınıf Örneklemesi (instantiation)

#Sınıf özellikleri barındıran alt küme oluşturulmasına bu isim verilir.

ali = VeriBilimci()

ali.sql
ali.deneyim_yili

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()

veli.sql
veli.bildigi_diller

#Örnek Özellikleri

class VeriBilimci:
    bildigi_diller = ["R", "Python"]
    bolum = ''
    def __init__(self):
        self.bildigi_diller = [] 

ali = VeriBilimci()
ali.bildigi_diller.append("Python") 
ali.bildigi_diller
ali.bolum = "End-müh"
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum = "makine müh"
veli.bolum """

#Örnek Metodları

class VeriBilimci:
    calisanlar = []
    
    def __init__(self):
        self.bildigi_diller = [] 
        self.bolum = ''
    
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil) 

# Örnek oluşturma
Ali = VeriBilimci()
Ali.bildigi_diller  
Ali.bolum  

Veli = VeriBilimci()
Veli.bildigi_diller  
Veli.bolum  

# Ali'ye yeni dil ekleme
Ali.dil_ekle("R")
Ali.bildigi_diller

#Miras Yapıları (inheritence)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Adress = ""
        
        
class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
        
veribilimci1 = DataScience()

       
class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""
    
marketingci1= Marketing()
