import HesapModulu

HesapModulu.yeni_maas(10000)

from HesapModulu import yeni_maas

HesapModulu.maaslar


#Hatalar

a=10
b=0

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("paydada sıfır olmaz")
    
a= 10
b="2"

a/b

try:
    print(a/b)
except TypeError:
    print("sayılar sayılarla bölünür")