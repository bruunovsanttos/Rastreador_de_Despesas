import classes
import argparse

def main():
    parser = argparse.ArgumentParser(description="Rastreador de Despesas")
    subparsers = parser.add_subparsers(dest="comando")

    parser_add = subparsers.add_parser("add", help="Adiciona uma nova despesa")
    parser_add.add_argument("--descricao", type=str, required=True, help="Descrição da despesa")
    parser_add.add_argument("--valor", type=float, required=True, help="Valor da despesa")
    parser_add.add_argument("--categoria", type=str, help="Categoria da despesa")

    parser_add = subparsers.add_parser("mostrar", help="Mostrar despesas")

    parser_add = subparsers.add_parser("deletar", help="Deleta uma despesa")
    parser_add.add_argument("--id", type=int, required=True, help="Id da despesa")



    args = parser.parse_args()

    rastreador = classes.RastreadorDeDespesas()  # Cria a instância do rastreador

    if args.comando == "add":
        # Chama o método de adicionar despesas passando os argumentos
        rastreador.adicionar_despesas(args.descricao, args.valor, args.categoria)
    elif args.comando == "mostrar":
        rastreador.mostrar_despesas()
    elif args.comando == "deletar":
        rastreador.excluir_despesas(args.id)

if __name__ == "__main__":
    main()