from abc import ABC, abstractmethod
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, sexo: Sexo, setor: Setor, salario: float, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.sexo = sexo
        self.setor = setor
        self.salario = salario
        self.data_nascimento = data_nascimento

        @abstractmethod
        def salario_final(self):
            pass

    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nEndereço: {self.endereco}"
            f"\nSexo: {self.sexo.nome} - {self.sexo.sigla}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: {self.salario:.3f}"
            f"\nData de nascimento: {self.data_nascimento}"
        )

