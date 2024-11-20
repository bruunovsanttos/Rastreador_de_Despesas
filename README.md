# Rastreador de Despesas

Neste projeto serão colocadas em práticas para que no fim seja entregue um rastreador de despesas via CLI.  
Este projeto esta na minha base de projetos retirados do site [Roadmap.sh](https://roadmap.sh/u/bruunovsanttos), estou seguindo os projetos da trilha de back-end.

## Requisitos de Projeto 📏📐
#### Funcionalidades Principais
1. Adicionar uma despesa com descrição, valor e categoria.
2. Atualizar uma despesa existente.   
3. Excluir uma despesa cadastrada.
4. Visualizar todas as despesas cadastradas.
5. Resumo geral das despesas.
6. Resumo das despesas de um mês específico.

#### Funcionalidades Adicionais
Exportação de despesas para arquivo CSV.  

Definição de um orçamento mensal e alertas para gastos próximos ou acima do limite.


## Ferramentas Do projeto 🔨🔧  
### Lingaugem de programação
#### Python 3.12  🐍
### Bibliotecas Utilizadas📚

[Argparse](https://docs.python.org/pt-br/3/library/argparse.html#module-argparse) a utilização dessa biblioteca consiste na maipulação correta dos argumentos dados pelo usuário do programa não havendo erros.  

[JSON](https://docs.python.org/pt-br/3/library/json.html) utilizada para a manipulação do arquivo que serve de base para as adiões e atulizações de despesas.  

[CSV](https://docs.python.org/pt-br/3/library/csv.html#module-csv) utilizada para a conversão dos dados para um arquivo CSV.  

[Datetime](https://docs.python.org/pt-br/3/library/datetime.html) utilizado para a atualização de datas do programa nos prints de criação e modificação.    

[OS](https://docs.python.org/pt-br/3/library/os.html#module-os) para manipulação de caminhos do programa e controle dos arquivos.    



# Estrutura do Projeto 📂  

rastreador_de_despesas.py: Arquivo principal que contém a lógica do programa.  

despesas.json: Arquivo que armazena os dados das despesas de forma persistente.  

despesas.csv: Arquivo exportado com as despesas, gerado sob demanda.  

comandos.png: Imagem com os comandos disponíveis (opcional).  



### Como Usar o Programa ▶️
Clone o repositório:  

   bash
         git clone https://github.com/seu-usuario/rastreador-de-despesas.git
         
Navegue até a pasta do projeto:

bash
cd rastreador-de-despesas
Execute o programa:
bash
python rastreador_de_despesas.py
### Comandos Disponíveis  
Os principais comandos para interação com o programa incluem:

|Comando|	Descrição|
|-------|------------|
|adicionar|	Adiciona uma nova despesa.|
|atualizar|	Atualiza uma despesa existente.|
|excluir|	Remove uma despesa.|
|listar|	Lista todas as despesas.|
|resumo|	Mostra um resumo geral das despesas.|
|mensal| Mostra despesas de um mês específico.|
|exportar|	Exporta despesas para CSV.|
|orcamento|	Define um teto de gastos mensais.|
  
### Exemplos de Uso 📖
1. **Adicionar uma nova despesa**:
   ```bash
   python rastreador_de_despesas.py adicionar --descricao "Supermercado" --valor 150.75 --categoria "Alimentação"
   

2. **Gerar resumo mensal:**

    ```bash
    python rastreador_de_despesas.py resumo --mes 11 
 

3. **Exportar dados para CSV:**

    ```bash
    python rastreador_de_despesas.py exportar  


### Contribuindo com o Projeto 🤝  
Contribuições são bem-vindas! Para contribuir:

Faça um fork do repositório.
Crie uma branch para sua funcionalidade:
bash
Copiar código
git checkout -b minha-nova-funcionalidade
Envie um Pull Request descrevendo suas alterações. 


### Próximas Melhorias 🌟
Refatoração do código para aumentar a legibilidade.
Adição de testes automatizados com unittest ou pytest.
Implementação de uma interface gráfica (GUI) como expansão futura.


### Licença 📜
Este projeto está licenciado sob a MIT License.

