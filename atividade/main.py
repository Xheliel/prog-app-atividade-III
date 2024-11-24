from models.endereco import Endereco
#from models.enums.bonificacao import Bonificacao
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.enums.unidade_federal import UnidadeFederativa
#from models.abstracts.cargo_confianca import CargoDeConfianca
from models.abstracts.funcionario import Funcionario
#from models.advogado import Advogado
#from models.diretor import Diretor
#from models.gerente import Gerente
from models.motorista import Motorista
import os

os.system("clear")

endereco_universal = Endereco("R Rua Python", "218", "Último andar", "40400-000", "Salvador", UnidadeFederativa.BAHIA)
motorista = Motorista("XXX.XXX.XXX.XX", "Carlos", "XXX.XXX.XXX-XX", "XX.XXX.XXX-XXX", endereco_universal, Sexo.MASCULINO, Setor.SAUDE, 3500, "XX/XX/XXXX")

print("Sistema 2.0")
print(motorista)
