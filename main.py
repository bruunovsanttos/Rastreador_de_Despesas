import classes
import argparse


def main():
    parser = argparse.ArgumentParser(description="Rastreador de Gastos")
    subparsers = parser.add_subparsers(dest="comando")

    parser_add = subparsers.add_parser("add", help="Adiciona nova tarefa")
    parser_add.add_argument("--descricao", type=str, required=True, help="Descrição da despesa")
    parser_add.add_argument("--valor", type=float, required=True, help="Valor da despesa")
    parser_add.add_argument("--categoria", type=str, help="Categoria da despesa")


    args= parser.parse_args()


    despesa = classes.Despesa()
    rastreador = classes.RastreadorDeDespesas()


    if args.comando == "add":
        despesa.AdicionarDespesas(args.descricao, args.valor, args.categotia)


    if __name__ == "__main__":
        main()