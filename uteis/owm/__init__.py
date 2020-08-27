import requests
import json


genero = None

def tempo(cidade):
    try:
        requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=+'+cidade+'&appid=d27521abffd26e6c1d772379c1d169d3')
        req2 = json.loads(requisicao.text)
        temper = float(req2['main']['temp']) - 273.15
        global genero

        try:
            if temper > 25:
               genero = 'pop'

            elif temper >= 10 and temper <= 25:
                 genero = 'rock'

            else:
                genero = 'classical'

        finally:
            return (f'\nA temperatura da cidade de \033[1;33m{cidade}\033[m é de \033[1;33m{temper:.1f}\033[m grau(s). \nComo sugestão indicamos uma playlist de \033[1;33m{genero}\033[m conforme abaixo:\n')
    except (KeyError, ValueError, TypeError):
        return ('\033[31mERRO: Cidade não encontrada!.\033[m')