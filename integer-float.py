#integer,float ve type fonksiyonu

sayi1 = 5   
sayi2 = 3,8
print(type(sayi1))  #tipini float mı int mi oldugunu yazdı

sayi1 = 5 ** 100 
sayi2 = 22 / 7 
print(sayi2)
# MATEMATİKSSEL İŞLEMLER
#toplama " + "
#cıkarma" - "
#carpma
#bölme
#tamsayı bölmesi
#kuvvet alma 
#mutlak deger "abs"
#yuvarlama "round"
#işlem önceligi

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(16 / 4)
print(3 // 4) # sadece tam kısmını verir
print(3 ** 4) 
print(abs(-3)) #ekrana iki yazar
print(abs(-3,16)) #3,16

sayi = 22 / 7
print(round(sayi))

sayi =3,874583
print(round(sayi,3)) # 3 basamak yuvarlar

print(3 * 5 + 6) #çarpma sonra toplama
print((3 + 2) * 4 + 3 )
 
 #KARŞILASTIRMA ÖPERATÖRLERİ
 eşittir " == "
 küçükütr " < "
 büyüktür " > "
 küçük eşittir " <= "
 büüyk essittir " >= "
 eşit degildir " ! "

sayi = 3
 print(3 == 3) # 3 eşit 3 ise true yazdırır

  sayi1 = 7
  sayi2 = 10
print(sayi1 < sayi2) #true 
print(sayi1 > sayi2) #false
print(sayi1 == sayi2) #false
print(sayi1 != sayi2) #true

a = 1
b = a 
a = 5
print(b) #1 

#string ve ıntegerları birbirinr çrvirme
sayi1 = "100"
sayi2 = 100
sayi3 = int(sayi1)
print(type(sayi1))  #class str
print(type(sayi2))  #class int 
print (sayi3 == sayi2) #true


sayi = 123
sayi2 = str(sayi)
print(sayi2) #123

sayi = 123
sayi2 = str(sayi)
print(type(sayi2))  #str


i = 1 
i = i + 2 # yada i += 2 kullanabiliriz
print(i) 





