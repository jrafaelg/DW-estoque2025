from sqlalchemy import create_engine

import app_categorias
from config import read_config

if __name__ == '__main__':
    config = read_config()
    engine = create_engine(url=config.url_bd, echo=False)


    while True:
        print("menu")
        print("==============================")
        print("1- listar categorias")
        print("2- adicionar categoria")
        print("3- modificar categoria")
        print("4- deletar categoria")
        print("0- finalizar")
        print("==============================")

        opcao = (input("digite: "))
        match opcao:
            case "1":
                app_categorias.listar(engine)

            case "2":
                app_categorias.adicionar(engine)

            case "3":
                app_categorias.modificar(engine)

            case "4":
                app_categorias.deletar(engine)

            case "0":
                exit(0)


