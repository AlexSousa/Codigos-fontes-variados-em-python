import sqlite3

db = sqlite3.connect("informacao.db")


def CriarTabela():
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists Admin(Nome text , Idade int)")


def Add(Nome, Idade):
    db.row_factory = sqlite3.Row
    db.execute("insert into Admin(Nome , Idade ) values(?,?)", (Nome, Idade))
    db.commit()
    print("Dados Gravados")


def DeletarDados(Nome):
    db.row_factory = sqlite3.Row
    db.execute("delete from Admin where Nome='{}' ".format(Nome))
    db.commit()
    print("Dados Apagados")


def ListarDados():
    cursor = db.execute("select * from Admin")
    for row in cursor:
        print("Nome:{},Idade:{}".format(row["Nome"], row["Idade"]))

def ModificarDados(Nome,Idade):
    db.row_factory=sqlite3.Row
    db.execute("update Admin set Idade=? where Nome=?",(Idade,Nome))
    db.commit()
    print("Modificacoes finalizadas")


def Principal():
    CriarTabela()
    while True:
        try:
            while True:
                op = int(input("Selecionar operacacao"))
                if op == 0:
                    break
                if op == 1:
                    Nome = input("Digite Seu nome")
                    Idade = input(("Digite sua idade"))

                    if ((Nome == "") or (Idade == "")):
                        print("Preencha todos os dados")
                        break
                    else:
                        Add(Nome, Idade)
                        return False
                elif op == 2:
                    ListarDados()
                    return False
                elif op == 3:
                    Nome = input("Escolha o nome para deletar")
                    DeletarDados(Nome)
                elif op == 4:
                    Nome=input("Digite o Novo Nome:")
                    Idade =int(input("Digite a nova idade"))
                    ModificarDados(Nome,Idade)

        except ValueError:
            print("Opcao não Existe", ValueError)


Principal()
