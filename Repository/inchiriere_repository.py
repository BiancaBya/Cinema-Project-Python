from Domain.inchiriere import Inchirieri
from Domain.film import Film
from Domain.client import Client
from Repository.film_repository import FilmRepository
from Repository.client_repository import ClientRepository


class InchirieriRepository:

    def __init__(self, film_repository: FilmRepository, client_repository: ClientRepository):
        self.__lista_inchirieri = []
        self.__film_repository = film_repository
        self.__client_repository = client_repository


    def get_toate_inchirierile(self):
        return self.__lista_inchirieri


    def add_inchiriere(self, film : Film, client : Client):
        inchiriere = Inchirieri(film, client)
        self.__lista_inchirieri.append(inchiriere)


    def delete_inchiriere(self, index):
        self.__lista_inchirieri.pop(index)


    def return_index(self, inchiriere : Inchirieri):
        return self.__lista_inchirieri.index(inchiriere)


    def find_inchiriere(self, id_client, id_film):
        for inchiriere in self.__lista_inchirieri:
            if inchiriere.get_film().get_id() == id_film and inchiriere.get_client().get_id() == id_client:
                return inchiriere
        return None







