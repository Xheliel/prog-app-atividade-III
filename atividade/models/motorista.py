from models.abstracts.funcionario import Funcionario
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.endereco import Endereco

class Motorista(Funcionario):
    def __init__(self, cnh: str, nome: str, cpf: str, rg: str, endereco: Endereco, sexo: Sexo, setor: Setor, salario: float, data_nascimento):
        super().__init__(nome, cpf, rg, endereco, sexo, setor, salario, data_nascimento)
        self.cnh = cnh

    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
            f"\nCNH: {self.cnh}"
        )