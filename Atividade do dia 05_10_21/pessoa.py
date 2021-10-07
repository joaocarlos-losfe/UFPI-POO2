class Pessoa:
    __slots__ = ['_nome', '_cpf', '_endereco', '_nascimento']

    def __init__(self, nome:str, cpf:str, endereco:str, nascimento:str):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._nascimento = nascimento

    @property
    def get_nome(self) -> str:
        return self._nome

    @property
    def get_endereco(self) -> str:
        return self._endereco

    @property
    def get_nascimento(self) -> str:
        return self._nascimento

    @property
    def get_cpf(self) -> str:
        return self._cpf

    def debug_infos(self):
        print(f"{self._nome} {self._cpf} {self._endereco} {self._nascimento}")