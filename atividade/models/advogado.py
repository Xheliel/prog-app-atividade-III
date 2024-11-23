from models.abstracts.funcionario import Funcionario
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.endereco import Endereco

class Advogado(Funcionario):
    def __init__(self, oab: str, nome: str, cpf: str, rg: str, endereco: Endereco, sexo: Sexo, setor: Setor, salario: float, data_nascimento):
        super().__init__(nome, cpf, rg, endereco, sexo, setor, salario, data_nascimento)
        self.oab = oab

    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
            f"\nOAB: {self.oab}"
        )