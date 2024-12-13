#Yan etkisiz fonksiyonlar

A=5

def impure_sum(b):
    return b+A

def pure_sum(a,b):
    return a+b

impure_sum(6)

#A'nın değeri değiştiğinde biz fonk. verdiğimiz değeri değiştirmesek de sonuç değişiyor bu yüzden impure bağımlıdır.

pure_sum(3,4)
#bu değişmez

#İsimsiz Fonksiyonlar

new_sum = lambda a,b : a+b
new_sum(5,7)

sirasiz_liste = [("b",3),("a",8),("d",12),("c",1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x: x[1])

#Vektorel Operasyonlar

a = [1,2,3,4]
b = [2,3,4,5]

ab=[]

for i in range(0, len(a)):
    ab.append(a[i]*b[i])
    
ab

#fp

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b 

#Map, filter ve reduce Fonksiyonları

liste = [1,2,3,4]

for i in liste:
    print(i+10)
    
    
list(map(lambda x: x+10, liste))
#map, verilen bir vektörün içerisinde bir fonksiyon çalıştırma imkanı verir

#filter iteratif nesne alır, başka bir iteratif nesne oluşrurur ve filtreler

list(filter(lambda x: x%2 == 0, liste))

#reduce indirgeme işlemi yapar

from functools import reduce

reduce(lambda a,b:a+b, liste)
