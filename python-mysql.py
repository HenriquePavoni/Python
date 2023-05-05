import mysql.connector

cnx = mysql.connector.connect(user='root', password='Pavoni77@',
                              host='localhost',
                              database='registro')

cursor = cnx.cursor()

flag = True

print("\n")

while flag == True:
    print("[1]Adicionar itens\n[2]Remover itens\n[3]Mostrar compras\n[4]Sair da Lista\n")

    cmd = input("O que deseja fazer ?: ")

    if cmd == "1":
        lista = list()
        
        lista.append(input("\nProduto: "))
        lista.append(input("\nQuantidade: "))
        lista.append(input("\nDescricao: "))

        print(lista)

        #Comando SQL add

        comando = ("INSERT INTO COMPRAS (PRODUTO, QUANTIDADE, DESCRICAO) VALUES (%s, %s, %s)")

        cursor.execute(comando, lista)
        cnx.commit()

    elif cmd == "2":
        lista = list()
        lista.append(input("\nQual produto deseja remover ?: "))

        print("\n")

        comando = ("DELETE FROM COMPRAS WHERE PRODUTO = %s")

        cursor.execute(comando, lista)
        cnx.commit()

    elif cmd == "3":

        cursor.execute("select * from COMPRAS")

        print("\n")

        for i in cursor.fetchall():
            print("="*40)
            print(f" Produto: {i[0]}\n Quantidade: {i[1]}\n Descricao: {i[2]}")
            print("="*40)
            print("\n")
    
    elif cmd == "4":
        flag = False
    
    else:
        print("\nErro\n")
