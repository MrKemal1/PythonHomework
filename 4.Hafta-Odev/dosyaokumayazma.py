with open("Yapay Zeka ile Python/Hafta4_Odev/odev.txt","a+",encoding="utf-8") as f:
    text=input("Lütfen bir metin giriniz: ")
    f.write(text+"\n")
    f.seek(0)
    print(f.read())
with open("Yapay Zeka ile Python/Hafta4_Odev/odev.txt","a+",encoding="utf-8") as f:    
        
    #lines = [input(f"Satır {i+1}: ") + "\n" for i in range(5)] 
    lines=[]
    for i in range(5):
        line=input(f"{i+1}. Satırı giriniz: ")
        lines.append((line+"\n"))
    
    f.writelines(lines)
    f.seek(0)
    
    myList=f.readlines()
    [print(item,end="") for item in myList]
