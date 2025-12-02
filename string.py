print("merhaba dünya!)
#stringler
#alt alta yazdırmak=
print("""merhaba
dünya""")
#alt satıra geçme

print("Merhaba\nDünya")
#\t boşluk olarak algılar
print("merhaba \t\tdünya")
##

mesaj="merhaba dünya"
print(mesaj)

## iki tırnak bosluk
mesaj = "merhaba"
mesaj2="dünya"
print(mesaj +" " + mesaj2)

##[] sayıya karsılık gelen karakter
mesaj = "Merhaba"
mesaj2="dünya"
print(mesaj[0])    #m bastan
print(mesaj[-3])   #a sondan
print(mesaj[0:4])  #0 karakterler 4 arasını yazar ilk sınır dahil ikinci degil= merh
print(mesaj[::2])  #ikişer ikişer artar =mraa
print(mesaj[::-1]) #ters yazar= abahrem

print(mesaj.upper()) #MERHABA
print(mesaj)  #merhaba

mesaj=mesaj.lower() merhaba
print(mesaj)      
  
mesaj=mesaj.capitalize()  Merhaba
print(mesaj) 

print(mesaj.starswith("me"))  false yazar 
print(mesaj.starswith("Me")) true yazar   # merhaba nasıl başladıgına bakar
print(mesaj.endswith("a")) true yazar   # nasıl bittigine bakar
print(len(mesaj + mesaj2))       #kaç karakter oldugunu bakar  12
print("merhaba" * 10)  # yan yana 10 tane merhaba yazar
##
isim="elif"
yas="20"
print("{} , {} yasındadır" .format (isim,yas))
##
isism="kübra"
mesaj="merhaba"

print("{} {} dedi...".format(isism,mesaj))
print(f"{isim} {mesaj} dedi") #f degişkeni 
##

