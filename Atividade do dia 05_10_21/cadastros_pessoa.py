from pessoa import Pessoa

class Cadastros:
    def __init__(self):
        self._cadastros = []

    def add_pessoa(self, pessoa:Pessoa):
        self._cadastros.append(pessoa)

    def get_pessoa(self, cpf:str)-> Pessoa:

        for pessoa in self._cadastros:
            if cpf == pessoa.get_cpf:
                return pessoa

        return None