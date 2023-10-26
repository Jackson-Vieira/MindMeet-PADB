import requests
from decouple import config

## make a simple terminal for the user to interact with 
## the program and requests to a api in "localhost:5000"

API_URL = config('API_URL')

class ClientHTTP:
    def __init__(self, api_url):
        self.url = api_url

    def get(self, path):
        return requests.get(self.url + path)

    def post(self, path, data):
        return requests.post(self.url + path, data=data)

    def put(self, path, data):
        return requests.put(self.url + path, data=data)

    def delete(self, path):
        return requests.delete(self.url + path)
    

client = ClientHTTP(API_URL)

def print_menu():
    print("-------- O que você deseja fazer? -------")
    print("1 - Operações com Agenda")

def print_agenda_usecases_menu():
    print("-------- Agenda Operacoes -------")
    print("1 - Listar agendas")
    print("2 - Agendas por id")
    print("3 - Criar agenda")
    print("4 - Deletar agenda")
    print("4 - Listar day hours de uma agenda")
    print("4 - Criar um day hour")
    print("5 - Editar um day hour")