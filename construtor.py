from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

pessoa1 = Pessoa(cpf=12345678901, nome="André", nascimento= date(1976,8,26), oculos=True)

marca1 = Marca(id=1, nome="Fiat", sigla="FIA")

veiculo1 = Veiculo(placa="LRW1127", cor="Cinza", peoprietario= pessoa1, marca=marca1)