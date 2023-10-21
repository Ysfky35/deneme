# print("Hello World")
# tekli yorum satırı 
""" çoklu yorum satırı  """

# değişken tanımlaması nasıl yapılır ?

# degiskenBir = "Yusuf"
# degisken_iki = "kızılarslan"

# 1sayı = 1 değişkenler sayı ile başlamaz 
#  sayı@ 2 özel karakter içermemeli 
# sayı 3 = 3#boşluk olamaz

# yas = 26  #büyük küçük harf duyarlılığı vardır 
# YAS = 30  #büyük küçük harf duyarlılığı vardır 

# print(yas)
# print(YAS)

# a,b,c = 10,15,20
# print(a,b,c)

# name = "kadir"
# print(type(name))
# print(type(yas))
# print(type(YAS))

# ogrenci = True
# print(ogrenci)

#*değişken nedir
# *değişken geçiçi olarak veri sakladığımız depoya bir alana değişken diyoruz.


# print(5000 + (5000*0.18))

# urun_a = 7000 
# kdv = 0,18
# print(urun_a + (urun_a *kdv))


# # TODO: uygulama
# """ Aşağıdaki ürünler için değişken oluşturup toplam bilgisini hesaplayınız  """
# ürün1 = 50
# ürün2 = 60 
# ürün3 = 152.40

# toplam (ürün1+ ürün2+ ürün3)
# print(toplam)

#!veri tipleri 

# int float 
# string
# list 
# tuple 
# dictionary 
# bool

#! sayı veri tipleri Int ve float 
#* py bir sayı tanımlaması yaparken kullanabileceğimiz 2 veri tipi vardır intger ve float veri tipleri intger tamsayı, float ise ondalıklı sayıdır. rakamdan sonra nokta varsa float olarak algılanır yoksa int olarak algılanır .

# print(2+2)
# print('2+2')
# print(type('2+2'))
# print(type(2))
# print(type(3+4))

#!string 
#* herhangi bir karakter dizesine string denir. Tek bir harften oluşacağı gibi bir çok harften ve rakamdan da oluşabilir 

# #!string slicing 
# print(ad[0:3]) #0-3 arasını yazdırır 3. index dahil değildir 
# print(ad[:3]) #yukarının aynısı 
# print(ad[5::]) #5. index'de başlar sonuna kadar gider.
# print(ad[::2]) # 0 başlar 2 artarak gider 
# print(ad[::-1]) #tersten yazar 
# ad = "Yusuf"
# soyad = "Kaya"
# şehir = "İzmir"

#!String metodları 
# * Upper metodu karakterleri büyük harfe çevirir 
 
 #*Strip metodu ile karakter dizisinin başındaki ve sonundaki boşlukları silebiliriz 

 #!string formatlama 
print("benim adım {}")

#TODO: uygulama 

website = "https://www.neosyazilim.com/"
kursAdi = "python Dersleri : Sıfırdan ileri Seviye python Programlama"

print(len(website))
print(len(kursAdi))

#*2 'website' içindeki www karakterlerini yazın 
print(website[8:11])

#*3 'website' içindeki com karakterini yazın 
print(website.index('c'))

print(kursAdi[0:15])
print(kursAdi[-18:])
print(kursAdi[::-1])

HelloWorld = " Hello World"
print(HelloWorld.title())

print("abc" *3)

print(kursAdi.lower())
print(website.startswith("www"))

#!listeler
#* liste elemanları sıralanabilir,güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir ve farklı veri tiplerindeki bilgileri barındırabilir.

mesaj = "merhaba dünya,ben yusuf".split()
print(mesaj)

isimler = ["ahmet",30,"mert",25"muhammed",24,"yusuf",31,"hakan",29,"atakan,21"]


#! liste slicing
print(isimler[0:3]) 
print(isimler[:3]) 


