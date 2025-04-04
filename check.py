import requests
import configparser
import sys

# Функция для загрузки USER_ID из config.ini
def get_user_id_from_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        user_id = config.get('Gifts', 'USER_ID')
        return user_id
    except (configparser.NoSectionError, configparser.NoOptionError):
        print("❌ Ошибка: Не удалось найти USER_ID в config.ini")
        return None

def check_username_availability(username):
    url = 'http://localhost:5000/check_username'
    payload = {'username': username}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Server error: {response.status_code}"}
    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to server"}

# Получаем USER_ID из config.ini

def cheker(test_username):
    if test_username:
        result = check_username_availability(test_username)
        print(f"Username: '{test_username}'")
        if 'valid' in result:

            print("Message:", result['reason'])
        else:
            print("Error:", result.get('error', 'Unknown error'))
        print("-" * 40)
    else:
        print("❌ Cannot check username: USER_ID not found in config.ini")
        sys.exit(1)
    return result['valid']
print(cheker(get_user_id_from_config()))