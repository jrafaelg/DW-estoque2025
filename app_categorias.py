from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from models import Categoria


def listar(engine: Engine):
    with Session(engine) as session:
        sentence = select(Categoria).order_by(Categoria.nome)
        registros = session.execute(sentence).scalars()
        print("id, nome, produtos, data de cadastro, data de atualizacao")
        for categoria in registros:
            print(f"{categoria.id}, {categoria.nome}, {len(categoria.lista_de_produtos)}, {categoria.dta_cadastro}, {categoria.dta_atualizacao}")

def selecionar_categoria(session: Session) -> Categoria:
    sentenca = select(Categoria).order_by(Categoria.nome)
    categorias = session.execute(sentenca).scalars()
    dicionario = dict()
    contador = 1
    for categoria in categorias:
        print(f"{contador} - {categoria.nome}")
        dicionario[contador] = categoria.id
        contador += 1

    id = int(input("Digite o ID do categoria: "))

    categoria = session.get_one(Categoria, dicionario[id])

    return categoria

def adicionar(engine: Engine):
    with Session(engine) as session:
        nome = input("Nome: ")
        categoria = Categoria()
        categoria.nome = nome
        session.add(categoria)
        try:
            session.commit()
        except:
            print("Erro ao adicionar")
        else:
            print("Adicionado com sucesso")


def modificar(engine):
    with Session(engine) as session:

        categoria = selecionar_categoria(session)

        # if categoria is None:

        nome = input("Novo nome: ")
        categoria.nome = nome

        try:
            session.commit()
        except:
            print("Erro ao atualizar")
        else:
            print("Atualizado com sucesso")


def deletar(engine):
    with Session(engine) as session:
        categoria = selecionar_categoria(session)

        session.delete(categoria)

        try:
            session.commit()
        except:
            print("Erro ao remover")
        else:
            print("Removido com sucesso")