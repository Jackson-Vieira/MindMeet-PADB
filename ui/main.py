import json
from abc import ABC, abstractmethod

import requests
from decouple import config

API_URL = config('API_URL')

class ClientHTTP:
    def __init__(self, api_url):
        self.headers = {'Content-type': 'application/json'}
        self.url = api_url

    def get(self, path):
        return requests.get(self.url + path)

    def post(self, path, data):
        return requests.post(self.url + path, data=data, headers=self.headers)

    def put(self, path, data):
        return requests.put(self.url + path, data=data, headers=self.headers)

    def delete(self, path):
        return requests.delete(self.url + path)
    

client = ClientHTTP(API_URL)

# def get_option_input(msg):
#     result = int(input(msg))
#     while result not in [1, 2, 3]:
#         result = int(input(msg))
#     return result


# TODO: http_client 
# TODO: improve menu options
class MenuFactory(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def print_menu(self):
        pass

    @abstractmethod
    def get_result(self, option):
        pass

class AgendaMenu(MenuFactory):
    def __init__(self, http_client: ClientHTTP) -> None:
        self.http_client = http_client
        self.allowed_options = [1, 2, 3, 4]

    def print_menu(self):
        print("\n-------- Agenda Operacoes -------")
        print("1 - Listar agendas")
        print("2 - Agendas por id")
        print("3 - Criar agenda")
        print("4 - Deletar agenda")
    
    def get_result(self, option):
        if option == 1:
            return self._list_agendas()
        elif option == 2:
            return self._get_agenda_by_id()
        elif option == 3:
            return self._create_agenda()
        elif option == 4:
            return self._delete_agenda()
        else:
            return None

    def _list_agendas(self):
        response = self.http_client.get("/agendas")
        data = response.json()
        keys = " | ".join(data[0].keys())
        print(keys)
        for i in range(len(data)):
            value = [str(item) for item in data[i].values()]
            print(" | ".join(value))
        

    def _get_agenda_by_id(self):
        agenda_id = int(input("Agenda ID: "))
        response = self.http_client.get(f'/agendas/{agenda_id}')
        if response.status_code == 404:
            print("Nao foi possivel encontrar a agenda!")
            return None
        print(response.json())

    # TODO: fix this method
    def _create_agenda(self):
        user_id = int(input("User ID: "))
        data = json.dumps({
            "psychologist_id": user_id
        })
        response = self.http_client.post('/agendas', data)
        if response.status_code == 201:
            print("Agenda criada com sucesso") 

    def _delete_agenda(self):
        agenda_id = int(input("Agenda ID: "))
        response = self.http_client.delete(f'/agendas/{agenda_id}')
        if response.status_code == 204:
            print("Agenda deletada com sucesso!")
            return
        if response.status_code == 404:
            print("Nao foi possivel encontrar a agenda!")
            return 
    
class MainMenu(MenuFactory):
    def __init__(self, http_client: ClientHTTP) -> None:
        self.http_client = http_client
        self.allowed_options = [1, 2]

    def print_menu(self):
        print("\n├── O que você deseja fazer?")
        print("├ 1 - Operações com Agenda")
        print("├ 2 - Sair")
    
    def get_result(self, option):
        if option == 1:
            return AgendaMenu(self.http_client)
        elif option == 2:
            return None

# TODO: validate only numbers
def option_input(msg) -> int:
    result = int(input(msg))
    while not result:
        result = int(input(msg))
    return result

def main(): 
    # TODO: tree menu effect
    http_client = ClientHTTP(API_URL)
    menu = MainMenu(http_client)
    option = 0
    while option != 5:
        menu.print_menu()
        option = option_input("├── Digite a opção: ")
        menu_option = menu.get_result(option)

        # stop loop
        if not menu_option:
            break

        menu_option.print_menu()
        option = option_input("├── Digite a opção: ")
        menu_option.get_result(option)

if __name__ == "__main__":
    main()