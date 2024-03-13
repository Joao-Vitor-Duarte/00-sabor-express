from fastapi import FastAPI,Query
import requests
app=FastAPI()
@app.get('/api/hello')
def hello():
    '''
        retorna hello world
    '''
    return{'hello':'world'}
@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes  
       
    '''
    url='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response=requests.get(url)
    if response.status_code==200:
        dados_json=response.json()
        dados_restaurante=[]
        if restaurante is None:
            return f'Dados:{dados_json}'
        for item in dados_json:
            if restaurante==item['Company']:
                dados_restaurante.append({
                    'item':item['Item'],
                    'preco':item['price'],
                    'descricao':item['description']
                })
        return {'Restaurante':f'{restaurante}','Cardapio': f'{dados_restaurante}'}
    else:
        return f'{response.status_code} - {response.text}'