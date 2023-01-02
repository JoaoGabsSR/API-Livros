class Books:
    def __init__(self, nome, autor, sinopse, genero):
        self._nome = self.validate_name(nome)
        self._autor = self.validate_autor(autor)
        self._sinopse = self.validate_sinopse(sinopse)
        self._genero = self.validate_genero(genero)
    
    @staticmethod
    def validate_name(name: str):
        try:
            if str.__len__(name) < 3:
                raise ValueError('Nome Inválido')
            elif name == '' or name == ' ':
                raise ValueError('Nenhum Nome Informado')
            else:
                return name
        except Exception as e:
            return e
    
    @staticmethod
    def validate_autor(autor: str):
        try:
            if autor == '' or autor == ' ':
                raise ValueError('Nenhum Nome Informado')
            else:
                return autor
        except Exception as e:
            return e
    
    @staticmethod
    def validate_sinopse(sinopse: str):
        try:
            if sinopse == '' or sinopse == ' ':
                return 'N/A'
            else:
                return sinopse
        except Exception as e:
            return e

    @staticmethod
    def validate_genero(genero: str):
        try:
            if genero == '' or genero == ' ':
                return 'N/A'
            else:
                return genero
        except Exception as e:
            return e

    def alter_name(self, name):
        try:
            self.nome = self.validate_name(name)
        except Exception as e:
            return e

    def alter_autor(self, autor):
        try:
            self.autor = self.validate_autor(autor)
        except Exception as e:
            return e

    def alter_sinopse(self, sinopse):
        try:
            self.sinopse = self.validate_sinopse(sinopse)
        except Exception as e:
            return e

    def alter_genero(self, genero):
        try:
            self.genero = self.validate_genero(genero)
        except Exception as e:
            return e

