class Livro:
    def __init__(self, codigo: int, titulo: str, autor: str, ano: int, disponivel: bool = True):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__disponivel = disponivel 

    @property
    def codigo(self): return self.__codigo
    
    @property
    def titulo(self): return self.__titulo
    
    @property
    def autor(self): return self.__autor
    
    @property
    def ano(self): return self.__ano
    
    @property
    def disponivel(self): return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            return True
        return False

    def to_dict(self):
        return {
            "codigo": self.__codigo,
            "titulo": self.__titulo,
            "autor": self.__autor,
            "ano": self.__ano,
            "disponivel": self.__disponivel
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            codigo=dados["codigo"],
            titulo=dados["titulo"],
            autor=dados["autor"],
            ano=dados["ano"],
            disponivel=dados["disponivel"]
        )
