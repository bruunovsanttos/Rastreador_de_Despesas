import datetime
import os
import json



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
        self.carregar_despesas()

    def carregar_despesas(self): #abre o json
        if os.path.exists(caminho_arquivo):
            with open("despesas.json", "r", encoding="utf-8") as arquivo:
                self.despesas = json.load(arquivo)

    def salvar_despesas(self): #salva o json
        with open("despesas.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.despesas, arquivo, indent=4)

    def GerarId(self):
        max((gasto['id'] for gasto in self.despesas), default=0) + 1
        return

    def DataAtual(self):
        data = datetime.now()
        data_formatada = data.strftime("%d/%m/%y %H:%M:%S")
        return data_formatada

    def adicionar_despesas(self):

        valor_gasto = float(input(f"Qual o valor da despesa?"))
        descricao_gasto = str(input(f"Descrição do gasto"))
        categoria_gasto = str(input(f"Em qual categoria deseja colocar o gasto?"))

        novo_gasto = {
        "id" : self.GerarId(),
        "valor" : valor_gasto,
        "descricao" : descricao_gasto,
        "categoria" : categoria_gasto,
        "data" : self.DataAtual(),
        "atualizado": self.DataAtual()
        }

        self.despesas.append(novo_gasto)
        self.salvar_despesas()

        print("Despesa salva com sucesso.")

    def MostrarDespesas(self):
        pass

    def ExcluirDespesas(self):
        pass

    def AlterarDespesa(self):
        pass

    def GastosTempo(self):
        pass








