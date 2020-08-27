from uteis import owm
import requests
import base64


def musica():
    client_id = 'd09bef5775114003b670cc814371766f' # your_client_id
    client_secret = 'be31b09cf993433b9977ab4cbe1f9cbb' # your_client_secret
    to_encode = client_id + ':' + client_secret
    base64_encoded_id_secret = base64.b64encode(to_encode.encode()).decode()

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic {}'.format(base64_encoded_id_secret)
    }

    params = {'grant_type': 'client_credentials'}

    r = requests.post('https://accounts.spotify.com/api/token', headers=headers, params=params)

    token = r.json()['access_token'] # Renova o Token a cada execução do programa.

    endpoint_url = "https://api.spotify.com/v1/recommendations?"

    # OUR FILTERS
    limit=20 # Listagem com até 20 músicas de seleção.
    market="US" # Código do País.
    seed_genres=owm.genero # Gênero musical.
    target_danceability=0.9

    query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

    response =requests.get(query,
                   headers={"Content-Type":"application/json", "Authorization":"Bearer {}".format(token)})

    json_response = response.json()

    for i in json_response['tracks']:
                print(f"Música: \033[1;34m{i['name']}\033[m Artista:\033[1;34m{i['artists'][0]['name']}\033[m")

