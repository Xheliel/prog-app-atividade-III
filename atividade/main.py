from models.endereco import Endereco
from models.enums.estado_civil import EstadoCivil
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.enums.unidade_federal import UnidadeFederativa
from models.abstracts.juridica import Juridico
from models.prestacao_servico import PrestacaoServico
from models.fornecedor import Fornecedor
from models.abstracts.fisica import Fisica
from models.cliente import Cliente
from models.abstracts.funcionario import Funcionario
from models.engenheiro import Engenheiro
from models.medico import Medico
from models.juridico import Juiz
import os

os.system("cls")

endereco1 = Endereco(
    "X XXXX XXXX", "XXX", "X XXXXX", "XXXXX-XXX", "XXXXXXXX", UnidadeFederativa.BAHIA
)
juridico1 = Juridico(
    "XXXXX", "XXXXX", 1, "XXXXXXXX", 18, "XX XXXXX XXXX", "XXXXX@XXXXX.XXX", endereco1
)
prestacao1 = PrestacaoServico(
    "01/01/2024",
    "31/12/2024",
    "XXXXX",
    "XXXXX",
    1,
    "XXXXXXXX",
    18,
    "XX XXXXX XXXX",
    "XXXXX@XXXXX.XXX",
    endereco1,
)
fornecedor1 = Fornecedor(
    "XXXXXX",
    "XXXXX",
    "XXXXX",
    1,
    "XXXXXXXX",
    18,
    "XX XXXXX XXXX",
    "XXXXX@XXXXX.XXX",
    endereco1,
)
fisica1 = Fisica(
    Sexo.MASCULINO,
    "21/08/2005",
    EstadoCivil.SOLTEIRO,
    1,
    "XXXXXXXX",
    18,
    "XX XXXXX XXXX",
    "XXXXX@XXXXX.XXX",
    endereco1,
)
cliente1 = Cliente(
    15,
    Sexo.MASCULINO,
    "21/08/2005",
    EstadoCivil.SOLTEIRO,
    1,
    "XXXXXXXX",
    18,
    "XX XXXXX XXXX",
    "XXXXX@XXXXX.XXX",
    endereco1,
)
funcionario1 = Funcionario(
    "XXX.XXX.XXX-XX",
    "XX.XXX.XXX.XXX",
    "XXXXXX",
    Setor.ENGENHARIA,
    3.500,
    Sexo.MASCULINO,
    "21/08/2005",
    EstadoCivil.SOLTEIRO,
    1,
    "XXXXXXXX",
    18,
    "XX XXXXX XXXX",
    "XXXXX@XXXXX.XXX",
    endereco1,
)
engenheiro1 = Engenheiro(
    "XXXXX",
    "XXX.XXX.XXX-XX",
    "XX.XXX.XXX.XXX",
    "XXXXXX",
    Setor.ENGENHARIA,
    3.500,
    Sexo.MASCULINO,
    "21/08/2005",
    EstadoCivil.SOLTEIRO,
    1,
    "XXXXXXXX",
    18,
    "XX XXXXX XXXX",
    "XXXXX@XXXXX.XXX",
    endereco1,
)
medico1 = Medico(
    "XXXXX",
    "XXX.XXX.XXX-XX",
    "XX.XXX.XXX.XXX",
    "XXXXXX",
    Setor.ENGENHARIA,
    3.500,
    Sexo.MASCULINO,
    "21/08/2005",
    EstadoCivil.SOLTEIRO,
    1,
    "XXXXXXXX",
    18,
    "XX XXXXX XXXX",
    "XXXXX@XXXXX.XXX",
    endereco1,
)
juiz1 = Juiz(
    "XXXXX",
    "XXX.XXX.XXX-XX",
    "XX.XXX.XXX.XXX",
    "XXXXXX",
    Setor.ENGENHARIA,
    3.500,
    Sexo.MASCULINO,
    "21/08/2005",
    EstadoCivil.SOLTEIRO,
    1,
    "XXXXXXXX",
    18,
    "XX XXXXX XXXX",
    "XXXXX@XXXXX.XXX",
    endereco1,
)
print(engenheiro1)
