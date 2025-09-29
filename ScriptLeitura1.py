import psutil
import pandas as pd
import time
from datetime import datetime

duracao = int(input("Digite a duração da captura: "))
contador = 0


arquivo_csv = "dados.csv"
processos = "processos.csv"

processos = []
data = []


print("\nIniciando monitoramento...")
print("\n------- CAPTURA DE CPU, RAM E DISCO -------")

while contador < duracao:
    user = psutil.users()[0].name
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent()  
    ram = psutil.virtual_memory().percent  
    disco = psutil.disk_usage("/").percent  

    dado = {
        'user': user
        ,'timestamp':timestamp
        ,'cpu': cpu
        ,'ram': ram
        ,'disco': disco
    }
 
    # Salva no CSV
    data.append(dado)


    print(f"\n Usuário: {user} | {timestamp} | CPU: {cpu}% | RAM: {ram}% | Disco: {disco}% |")
  

    for proc in psutil.process_iter():
        dado = {
        'timestamp':timestamp
        ,'processo': proc.name()
        ,'pid': proc.pid
        ,'cpu':proc.cpu_percent()
        ,'ram': round(proc.memory_percent(),4)
    }
        processos.append(dado)

    contador+=1
    time.sleep(1)


df1 = pd.DataFrame(data = data)

df1.to_csv('data.csv',sep=';')

df = pd.DataFrame(data = processos)

df.to_csv('processos.csv',sep=';')

print("\n------- CAPTURA DE PROCESSOS -------\n")
print(df) 


print("Finalizando monitoramento...")
