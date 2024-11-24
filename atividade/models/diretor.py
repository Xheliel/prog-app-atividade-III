from atividade.models.enums.bonificacao import Bonificacao
from models.abstracts.cargo_confianca import CargoDeConfianca
from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.endereco import Endereco
from models.abstracts.funcionario import Funcionario
from abc import ABC, abstractmethod

class Diretor(CargoDeConfianca, Funcionario):
    def __init__(self, bonificacao: Bonificacao, nome: str, cpf: str, rg: str, endereco: Endereco, sexo: Sexo, setor: Setor, salario: float, data_nascimento):
        super().__init__(bonificacao, nome, cpf, rg, endereco, sexo, setor, salario, data_nascimento)
    
    class Contratacao(ABC):
        @abstractmethod
        def admitir(self):
            pass

        def demitir(self):
            pass

    def salario_final(self):
        PREMIO = 0.5
        return PREMIO + Bonificacao.DIRETOR.value * self.salario

    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
            f"\n{self.salario_final():.2f}"
        )