import datetime


class Despesa:
    def __init__(self, id, descricao, valor, categoria=None):
        self.id = id
        self.data = datetime.now()strftime('d%-m%-Y%')
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

    def __str__(self):
        return f"{self.id} - {self.data} - {self.descricao} - R${self.valor:.2f} - Categoria: {self.categoria or 'Não definida'}"


class RastreadorDeDespesas:

    def __init__(self):
        self.despesas = []

    def CarregarDespesas(self): #abreo json
        pass

    def SalvarDesperas(self): #salva o json
        pass

    def AdicionarDespesas(self):
        pass

    def MostrarDespesas(self):
        pass

    def ExcluirDespesas(self):
        pass

    







