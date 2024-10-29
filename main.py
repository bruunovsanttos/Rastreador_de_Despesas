import classes
import argparse


def main():
    parser = argparse.ArgumentParser(description="Rastreador de Gastos")
    subparsers = parser.add_subparsers(dest="comando")

    parser_add = subparsers.add_parser("add", help="Adiciona nova tarefa")
    parser_add.add_argument("descrição", type=str, help="Descrição de tarefa")


    args= parser.parse_args()


    despesa = classes.Despesa()
    rastreador = classes.RastreadorDeDespesas()


    if args.comando == "add":
        despesa.AdicionarDespesas(args.descricao, args.valor, args.categotia)


    if __name__ == "__main__":
        main()