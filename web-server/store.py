import requests

def get_categories():
    #ruta donde queremos hacer la solicitud
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json() #transformar a formato json
    for category in categories:
        print(category['name'])