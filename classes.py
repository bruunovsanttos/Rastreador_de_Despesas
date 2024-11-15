from datetime import datetime
import os
import json
import csv

categorias = ["Alimentação", "Transporte", "Lazer", "Saúde", "Educação"]


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
        self.orcamento_mensal = 0.0
        self.carregar_despesas()

    def carregar_despesas(self):  # abre o json
        if os.path.exists(caminho_arquivo):
            with open("despesas.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                self.despesas = dados.get("despesas", [])
                self.orcamento_mensal = dados.get("orcamento_mensal", 0.0)

    def salvar_despesas(self):
        dados = {
            "orcamento_mensal": self.orcamento_mensal,
            "despesas": self.despesas
        }
        with open("despesas.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4)


    def gerar_id(self):
        ids_validos = []

        for despesa in self.despesas:
            if despesa['id'] is not None:
                ids_validos.append(despesa['id'])

        if not ids_validos:
            return 1
        else:
            return max(ids_validos) + 1

    def data_atual(self):
        data = datetime.now()
        data_formatada = data.strftime("%d/%m/%Y %H:%M:%S")
        return data_formatada

    def adicionar_despesas(self, descricao, valor, categoria):

        self.carregar_despesas()

        total_atual=0
        for despesa in self.despesas:
            total_atual += despesa['valor']

        if total_atual + valor > self.orcamento_mensal:
            print(f"O valor {valor:.2f} vai exceder o total de gastos de {self.orcamento_mensal}")
            return


        novo_gasto = {
        "id" : self.gerar_id(),
        "valor" : valor,
        "descricao" : descricao,
        "categoria" : categoria,
        "data" : self.data_atual(),
        "modificado": self.data_atual()

        }
        if categoria not in categorias:
            print(f"Categoria invalida, você deve escolher categoria entre:", categorias)
            return

        self.despesas.append(novo_gasto)
        self.salvar_despesas()

        print("Despesa salva com sucesso.")

    def mostrar_despesas(self, categoria = None):
        self.carregar_despesas()

        if categoria:
            if categoria not in categorias:
                print(f"Categoria: {categoria} invalida. As categorias são: {categorias}")

            despesas_categoria = []

            for despesa in self.despesas:
                if despesa['categoria'] == categoria:
                    despesas_categoria.append(despesa)

            if despesas_categoria:
                for despesa in despesas_categoria:
                    print(f"Id: {despesa['id']} \n Descrição: {despesa['descricao']} \n Valor: {despesa['valor']:.2f} \n Data: {despesa['data']} \n Categoria: {despesa['categoria']} \n Modificado em: {despesa['modificado']}")

            else:
                print(f"Não há despesas cadastradas para a categoria {categoria}")
        else:
            if not self.despesas:
                print("Não há despesas para mostrar")
                return

            for despesa in self.despesas:
                print(f"Id: {despesa['id']} \n Descrição: {despesa['descricao']} \n Valor: {despesa['valor']:.2f} \n Data: {despesa['data']} \n Categoria: {despesa['categoria']} \n Modificado em: {despesa['modificado']}")


    def excluir_despesas(self, id):
        self.carregar_despesas()

        despesa_encontrada = False

        for despesa in self.despesas:
            if despesa['id'] == id:
                self.despesas.remove(despesa)
                print(f"Despesa {despesa['id']}, {despesa['descricao']} deletada com sucesso.")
                despesa_encontrada = True
                break

        if not despesa_encontrada:
            print("Não ha nenhuma despesa com este ID.")

        self.salvar_despesas()
    #def excluir_despesas(self, id):
    #self.carregar_despesas()

    #for despesa in self.despesas == 'id':
    #    if not id in despesas:
     #       print("Não há nenhuma despesa com este ID.")
      #  else:
       #     self.despesas.remove(despesa)
        #    print(f"Despesa {despesa['id']}, {despesa['descricao']} deletada com sucesso.")
         #   break


    def alterar_despesa(self, id):
        self.carregar_despesas()

        despesa_encontrada  = False

        for despesa in self.despesas:
            if despesa['id'] == id:
                despesa['descricao'] = str(input("Qual descrição você deseja colocar agora?"))
                despesa['valor'] = novo_valor = float(input("qual o valor gasto?"))
                if novo_valor <0:
                    print("O novo valor não pode ser negativo")
                    return
                despesa['modificado'] = self.data_atual()
                despesa_encontrada = True
                print(f"A desepsa {despesa['id']} foi alterada como {despesa['descricao']} e valor de {despesa['valor']} modificado em {despesa['modificado']}.")
                break

        if not despesa_encontrada:
            print("Não ha nenhuma despesa com este ID.")

        self.salvar_despesas()


    def gastos_tempo(self):
        pass

    def resumo_gastos_totais(self):
        total = 0
        for despesa in self.despesas:
            total += despesa['valor']
        print(f"Total de despesas é de: R${total:.2f}")

    def resumo_mensal(self, mes):
        total_mensal = 0  # Inicializa o total mensal como zero
        for despesa in self.despesas:  # Itera sobre cada despesa
            # Extrai o mês da data da despesa
            mes_despesa = int(despesa['data'].split("/")[1])
            if mes_despesa == mes:  # Verifica se o mês da despesa é igual ao mês desejado
                total_mensal += despesa['valor']  # Adiciona o valor da despesa ao total mensal
        print(f"Total de despesas para o mês {mes}: R${total_mensal:.2f}")  # Exibe o total mensal formatado

    def definir_orcamento(self):
        valor = float(input("Digite um valor para o gasto mensal desejado: "))
        if valor < 0:
            print("A meta de gastos não pode ser negativa")
            return
        self.orcamento_mensal = valor
        self.salvar_despesas()
        print(f"O Teto de gastos foi definido em R$:{valor:.2f}.")

    def exportar_csv(self):
        if os.path.exists(caminho_arquivo):
            with open ("despesas.csv", mode= "w", newline='', encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)

                escritor.writerow(['ID', 'Descrição', 'Valor', 'Categoria', 'Data', 'Modificado'])
                for despesa in self.despesas:
                    escritor.writerow([despesa['id'], despesa['descricao'], despesa['valor'], despesa['categoria'], despesa['data'],despesa['modificado']])
                    
            print("Arquivo exportado com sucesso")





