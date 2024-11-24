from atividade.models.enums.bonificacao import Bonificacao
from models.abstracts.cargo_confianca import CargoDeConfianca
from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.endereco import Endereco

class Gerente(CargoDeConfianca):
    def __init__(self, bonificacao: Bonificacao, nome: str, cpf: str, rg: str, endereco: Endereco, sexo: Sexo, setor: Setor, salario: float, data_nascimento):
        super().__init__(bonificacao, nome, cpf, rg, endereco, sexo, setor, salario, data_nascimento)

    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
        )