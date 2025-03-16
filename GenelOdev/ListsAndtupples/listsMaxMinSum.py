sayilar=[]
for i in range(5):
    sayi=int(input(f"{i+1}. sayıyı giriniz: "))
    sayilar.append(sayi)

toplam=sum(sayilar)
ortalama=toplam/len(sayilar)
enBuyuk=max(sayilar)
enKucuk=min(sayilar)

print(f"Listenin Toplamı: {toplam}")
print(f"Listenin ortalaması: {ortalama}")
print(f"Listenin en küçük elemanı: {enKucuk}")
print(f"Listenin en büyük elemanı: {enBuyuk}")
