import datetime
import os
import json
import argparse


diretorio = "C:/Users/bruvieira/Desktop/Nova_pasta/Rastreador_de_despesas/Rastreador_de_Despesas"
nome_arquivo = "despesas.json"
caminho_arquivo = os.path.join(diretorio, nome_arquivo)


class Despesa:
    def __init__(self, id, data, descricao, valor, categoria=None):
        self.id = id
        self.data = datetime.now()strftime('d%-m%-Y%') #ARRUMAR ESSA BAZORDIA BRUNO!!!!!
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

    def __str__(self):
        return f"{self.id} - {self.data} - {self.descricao} - R${self.valor:.2f} - Categoria: {self.categoria or 'Não definida'}"


class RastreadorDeDespesas:

    def __init__(self):
        self.despesas = []

    def CarregarDespesas(self): #abre o json
        if os.path.exists(caminho_arquivo):
            with open("despesas.json", "r", encoding="utf-8") as arquivo:
                self.despesas = json.load(arquivo)

    def SalvarDesperas(self): #salva o json
        with open("despesas.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.despesas, arquivo, indent=4)

    def AdicionarDespesas(self, valor, descricao, categoria):
        CarregarDepesas()

        gastos = []

        valor = float(input(f"Qual o valor da despesa?"))
        descricao = str(input(f"Descrição do gasto"))
        categoria = str(input(f"Em qual categoria deseja colocar o gasto?"))

        novo_gasto = {
        "id" = #tem que fazer a def do id ainda
        "valor" = valor
        "descricao" = descricao
        "categoria" = categoria
        "data" = # fazer a def de data
        }
        
        SalvarDespesas()

    def MostrarDespesas(self):
        pass

    def ExcluirDespesas(self):
        pass









