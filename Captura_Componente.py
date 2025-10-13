import psutil
import platform
import mysql.connector as mysql



# Informações do SO

nomeSo = platform.system()
realeaseSo = platform.release()
versaoSO = platform.version()
processador = platform.processor()
nucleosFisicos = psutil.cpu_count(logical=False)
nucleosLogicos = psutil.cpu_count(logical=True)
nomeMaquina = platform.node()

print(processador)
print("Credenciais do banco de dados MySQL")
opcaouser = input("Digite seu usuario:")
opcaopassword = input("Digite sua senha:")
opcaodatabase = input("Digite o nome da db:")
 

try:
    conexao = mysql.connect(
                host="localhost",      
                user=opcaouser,
                password=opcaopassword,
                database=opcaodatabase
            )

    cur = conexao.cursor()



except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
    exit()


print("\n")
print("\n=== Iniciando Captura de componentes ===")


uso = psutil.cpu_percent(interval=1) 
ramTotal = round(psutil.virtual_memory().total / (1024**3),2)
ramUsada = psutil.virtual_memory().percent
discoTotal = round(psutil.disk_usage("/").total / (1024**3),2)
discoUsado = psutil.disk_usage("/").percent

print(f"Nome da Máquina: {nomeMaquina} | CPU: {uso}% | Ram total: {ramTotal}GB | Ram em Uso: {ramUsada}% | Disco total: {discoTotal}GB | Disco em uso: {discoUsado}%")




cur.execute(f"insert into componente (tipo, fk_servidor) select 'CPU', id from servidor where nome_maquina = '{nomeMaquina}';")
conexao.commit()
cur.execute(f"insert into componente (tipo, fk_servidor) select 'RAM', id from servidor where nome_maquina = '{nomeMaquina}';")
conexao.commit()
cur.execute(f"insert into componente (tipo, fk_servidor) select 'DISCO', id from servidor where nome_maquina = '{nomeMaquina}';")
conexao.commit()

print("\n=== Captura finalizada ===")