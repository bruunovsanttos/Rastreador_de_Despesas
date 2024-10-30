from datetime import datetime
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

    def gerar_id(self):
        ids_validos = []  # Inicializa uma lista vazia para IDs válidos

        for despesa in self.despesas:
            if despesa['id'] is not None:  # Verifica se o ID não é None
                ids_validos.append(despesa['id'])  # Adiciona IDs válidos à lista

        if not ids_validos:  # Se não houver IDs válidos
            return 1
        else:
            return max(ids_validos) + 1  # Retorna o maior ID + 1

    def data_atual(self):
        data = datetime.now()  # Agora está correto
        data_formatada = data.strftime("%d/%m/%Y %H:%M:%S")
        return data_formatada

    def adicionar_despesas(self, descricao, valor, categoria):

        self.carregar_despesas()

        novo_gasto = {
        "id" : self.gerar_id(),
        "valor" : valor,
        "descricao" : descricao,
        "categoria" : categoria,
        "data" : self.data_atual(),

        }

        self.despesas.append(novo_gasto)
        self.salvar_despesas()

        print("Despesa salva com sucesso.")

    def mostrar_despesas(self):
        self.carregar_despesas()

        if not self.despesas:
            print("Não ha despesas para mostrar.")
            return
            
        for despesa in self.despesas:
            print(f"Id: {despesa['id']} \n Descrição: {despesa['descricao']} \n Valor: {despesa['valor']:.2f} \n Data: {despesa['data']} \n Categoria: {despesa['categoria']}")

    def excluir_despesas(self):
        pass

    def alterar_despesa(self):
        pass

    def gastos_tempo(self):
        pass








