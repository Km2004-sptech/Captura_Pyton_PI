import platform
import mysql.connector as mysql

print("Credenciais do banco de dados MySQL")
opcaouser = input("Digite seu usuario:")
opcaopassword = input("Digite sua senha:")
opcaodatabase = input("Digite o nome da db:")

try:
    conexao = mysql.connect(
                host="localhost",      
                user=opcaouser,
                password=opcaopassword,
                database=opcaodatabase,
            )

    cur = conexao.cursor()



except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
    exit()

nomeMaquina = platform.node()

cur.execute(f"insert into servidor (nome_maquina) values ('{nomeMaquina}')")
conexao.commit()