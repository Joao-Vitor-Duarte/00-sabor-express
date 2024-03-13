import requests
import json
url='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response=requests.get(url)
if response.status_code==200:
    dados_json=response.json()
    dados_restaurante={}
    for item in dados_json:
        nome_restaurante=item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante]=[]
        dados_restaurante[nome_restaurante].append({
            'item':item['Item'],
            'preco':item['price'],
            'descricao':item['description']
        })
    for nome_restaurante,dados in dados_restaurante.items():
        nome_do_arquivo=f'{nome_restaurante}.json'
        with open(nome_do_arquivo,'w') as file:
            json.dump(dados,file,indent=4)
else:
    print(f'o erro foi {response.status_code}')