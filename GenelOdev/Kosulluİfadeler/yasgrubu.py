yas=int(input("Yaşınızı giriniz: "))

if yas<=12:
    print("Çocuk")
elif yas<=19 and yas>=13:
    print("Genç")
elif yas<=59 and yas>=20:
    print("Yetişkin")
elif yas>59:
    print("Yaşlı")