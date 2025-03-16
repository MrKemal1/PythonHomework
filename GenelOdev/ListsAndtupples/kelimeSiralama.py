kelimeler=[]
for i in range(5):
    kelime=(input(f"{i+1}. kelimeyi giriniz: "))
    kelimeler.append(kelime)
    
kelimeler.reverse()
print(kelimeler[::-1])