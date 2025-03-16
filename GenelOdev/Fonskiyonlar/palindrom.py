def palindrom(kelime):
    
    if kelime[::-1]==kelime:
        print(f"{kelime} kelimesi palindromdur")
    else:
        print(f"{kelime} kelimesi palindrom değildir")
        
palindrom("Ey edip adanada pide ye")

