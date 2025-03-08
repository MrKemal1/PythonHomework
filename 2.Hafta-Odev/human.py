class Human:
    
    def __init__(self,name):
        self.name = name
        print("A human instance was produced")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        name="Ahmet"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking")
        