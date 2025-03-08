#alias = takma ad
from matematik import topla as ToplamaIslemi
from day2 import sayHello
from human import Human

from selenium import webdriver  
#built-in modules
import random
#packages
print("*********************************")
print(ToplamaIslemi(20,12))
print(random.randint(0,100))

human1= Human("Mustafa")
human1.talk("Hi!")
chromeDriver = webdriver.Chrome()