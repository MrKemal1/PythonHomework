from human import Human


faiz = 1.59
vade= "36"
krediAdi= "İhtiyaç Kredisi"


print(type(faiz))
print(type(vade))
print(type(krediAdi)),


print(int(vade)+12)
# print(int(krediAdi))
faiz  = str(faiz)
print(type(faiz))

# vade = int(input("Lütfen istediğiniz vade sayısını giriniz:   "))
# print(type(vade))
# vade = vade + 12

#string interpolation
#Seçtiğiniz vade sonucu ortaya çıkan vade: 
print("Seçtiğiniz vade sonucu ortaya çıkan vade: "+ str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade:  {vadeSayisi}" .format(vadeSayisi=vade) )


isim="Ali"
metin= "Merhaba {name}".format(name=isim)
print(metin)


#f-string
metin=f"Hosgeldiniz"
print(metin)

#listeler
#döngüler
#fonsiyonlar

krediler = [" İhtiyaç Kredisi" ,"Taşıt Kredisı" ,"Konut Kredisi"]
print(type(krediler))

print(krediler[0])
print(len(krediler)) #length
#print(krediler[3]) hata verir

krediler.append("Özel Kredi") #listenin sonuna ekler
print(krediler)

krediler.pop(0) #Belirttiğin indexteki değeri siler default olarak sondakini siler
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)
krediler.remove("Taşıt Kredisi") #Remove değer bazlı çalışır ve listede değerle ilk eşleşen elemanı siler
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"]) #Listeye birden çok eleman ekler


#for 
#i = 0   i < 10
print("******************************************")

for kredi in krediler:
    print(kredi)

for i in range(3):
    print(krediler[i])

print("******************************************")

for i in range(len(krediler)):
    print(krediler[i]) 

print("******************************************")

i=0
while i < 10:
    print(i)
    i+=1
print("******************************************")

while True:
    print("x")
    break

print("******************************************")

while i < len(krediler):
    if krediler[i]=="Konut Kredisi":
        break
    print(krediler[i])
    i+=1


print("*********************")

#fonksiyonlar

fiyat = 100
indirim= 20
yenfiyat=fiyat - indirim

#definition define

def calculate():
    print(100-20)
    
calculate()
calculate()

def calculateWithParams(a,b):
    print(a-b)

calculateWithParams(100,35)

def sayHello(name):
    print(f"Merhaba {name}")
    
sayHello("Ali")
sayHello("Kemal")

#Geriye Değer Döndüren Fonskisyonlar

def calculateAndReturn(price,discount):
    return price-discount


newPrice = calculateAndReturn(100,30)

print(newPrice)


print("*********************")

def calculatePriceAndReturn(price,discount):
    return price-discount

def calculatePrice(price,discount):
    print(price - discount)
    
print("*********************")

fonk1= calculatePrice(100,10)
fonk2= calculatePriceAndReturn(100,59)
print(fonk1)
print(fonk2)
print("*********************")


# sınıflar => classes
# modules
# paket yönetimi


human1= Human("Ali")
human1.talk("Merhaba!")
human1.walk()
print(human1)
human2 = Human("Kemal")
human2.talk("Naber") 
human2.walk()

        
