from Ui.consola import Consola
from Repository.film_repository import FilmRepository
from Repository.client_repository import ClientRepository
from Repository.inchiriere_repository import InchirieriRepository
from Service.film_service import FilmService
from Service.client_service import ClientService
from Service.inchiriere_service import InchiriereService
from Tests.teste import Teste


film_repository = FilmRepository()
client_repository = ClientRepository()
inchirieri_repository = InchirieriRepository(film_repository,client_repository)
film_service = FilmService(film_repository)
client_service = ClientService(client_repository)
inchirieri_service = InchiriereService(film_repository, client_repository, inchirieri_repository)
runner = Consola(film_service, client_service, inchirieri_service)

film_repository_test = FilmRepository()
client_repository_test = ClientRepository()
inchirieri_repository_test = InchirieriRepository(film_repository_test, client_repository_test)
test = Teste(film_repository_test, client_repository_test, inchirieri_repository_test)

test.run_teste()
runner.run()






