from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from app_categorias import selecionar_categoria
from models import Produto, Categoria


# id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
# nome = Column(String(256), nullable=False)
# preco = Column(DECIMAL(precision=10, scale=2), default=0.00)
# estoque = Column(Integer, default=0)
# ativo = Column(Boolean, nullable=False, default=True)
# #

def listar(engine: Engine):
    with Session(engine) as session:
        sentence = select(Produto).order_by(Produto.nome)
        registros = session.execute(sentence).scalars()
        print("id, nome, categoria, preco, estoque, ativo")
        for produto in registros:
            print(f"{produto.id}, {produto.nome}, {produto.categoria.nome}, {produto.preco}, {produto.estoque}, {"Ativo" if produto.ativo else "Inativo"}")



def adicionar(engine: Engine):
    with Session(engine) as session:
        nome = input("Nome: ")
        preco = input("Preco: ")
        estoque = input("Estoque: ")
        ativo = input("Ativo: (S/N) ").lower()
        ativo = True if ativo == "s" else False


        categoria = selecionar_categoria(session)

        produto = Produto()
        produto.categoria = categoria
        produto.nome = nome
        produto.preco = preco
        produto.estoque = estoque
        produto.ativo = ativo

        session.add(produto)

        try:
            session.commit()
        except:
            print("Erro ao adicionar")
        else:
            print("Adicionado com sucesso")





def modificar(engine):
    with Session(engine) as session:
        sentenca = select(Produto).order_by(Produto.nome)
        produtos = session.execute(sentenca).scalars()
        dicionario = dict()
        contador = 1
        for produto in produtos:
            print(f"{contador} - {produto.nome}")
            dicionario[contador] = produto.id
            contador += 1

        id = int(input("Digite o ID do produto: "))

        produto = session.get_one(Produto, dicionario[id])

        # if produto is None:

        nome = input("Nome: ")
        preco = input("Preco: ")
        estoque = input("Estoque: ")
        ativo = input("Ativo: (S/N) ").lower()
        ativo = True if ativo == "s" else False

        categoria = selecionar_categoria(session)

        produto.categoria = categoria
        produto.nome = nome
        produto.preco = preco
        produto.estoque = estoque
        produto.ativo = ativo

        try:
            session.commit()
        except:
            print("Erro ao atualizar")
        else:
            print("Atualizado com sucesso")


def deletar(engine):
    with Session(engine) as session:
        sentenca = select(Produto).order_by(Produto.nome)
        produtos = session.execute(sentenca).scalars()
        dicionario = dict()
        contador = 1
        for produto in produtos:
            print(f"{contador} - {produto.nome}")
            dicionario[contador] = produto.id
            contador += 1

        id = int(input("Digite o ID do produto que será excluído: "))

        produto = session.get_one(Produto, dicionario[id])

        session.delete(produto)

        try:
            session.commit()
        except:
            print("Erro ao remover")
        else:
            print("Removido com sucesso")