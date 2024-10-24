class Despesa:
    def __init__(self, id, data, descricao, valor, categoria=None):
    self.id = id
    self.data = data 
    self.descricao = descricao
    sel.valor = valor
    self.categoria = categoria

    def __str__(self):
        return f"{self.id} - {self.data} - {self.descricao} - R${self.valor:.2f} - Categoria: {self.categoria or 'Não definida'}"


