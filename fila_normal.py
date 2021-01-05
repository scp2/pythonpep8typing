class filanormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhatual:str = ""

    def gerarsenhaatual(self)->None:
        self.senhatual = f'NM{self.codigo}'