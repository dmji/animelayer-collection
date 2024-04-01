import json
import requests
import os
from src.const_parameters import *

def readLogindata(path):
    if(not os.path.exists(path)):
        login_data = {
            'login': "",
            'password': ""
        } 
        with open(path, 'w') as file:
            json.dump(login_data, file)
        return None
    
    login_data = None
    with open(path, 'r') as file:
        login_data = json.load(file)
    return login_data
    
def createSessionWithLogin(login_data):
    login_data = readLogindata(LOGIN_DATA_JSON)
    if(login_data == None):
        return None
    
    session = requests.Session()

    # Отправляем POST-запрос
    response = session.post(LOGIN_URL, data=login_data)
    # Проверяем успешность авторизации
    if response.status_code == 200:
        print("Успешно выполнен вход на сайт")
        return session
    else:
        print("Ошибка при входе на сайт")
        return None