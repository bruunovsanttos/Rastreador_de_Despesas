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
        self.data = self.DataAtual()
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

    def GerarId(self):
        max(gasto['id'] for gasto in gastos) + 1
        return

    def DataAtual(self):
        data = datetime.now()
        data_formatada = data.strftime("%d/%m/%y %H:%M:%S")
        return data_formatada

    def AdicionarDespesas(self):
        self.CarregarDespesas()

        gastos = []

        valor_gasto = float(input(f"Qual o valor da despesa?"))
        descricao_gasto = str(input(f"Descrição do gasto"))
        categoria_gasto = str(input(f"Em qual categoria deseja colocar o gasto?"))

        novo_gasto = {
        "id" : self.GerarId(),
        "valor" : valor_gasto,
        "descricao" : descricao_gasto,
        "categoria" : categoria_gasto,
        "data" : self.DataAtual()
        }

        gastos.append(novo_gasto)


        self.SalvarDespesas()

    def MostrarDespesas(self):
        pass

    def ExcluirDespesas(self):
        pass









