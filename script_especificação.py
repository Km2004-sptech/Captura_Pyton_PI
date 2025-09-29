import psutil
import pandas as pd
import time
from datetime import datetime

duracao = int(input("Digite a duração da captura: "))
contador = 0
qtdParticoes = 0

data = []



print("\n------- CAPTURANDO HARDWARE -------")



swapTotal = round(psutil.swap_memory().total / (1024**3),2)
ramTotal = round(psutil.virtual_memory().total / (1024**3),2)
discoTotal = round(psutil.disk_usage("/").total / (1024**3),2)
Particoes = psutil.disk_partitions()
nucleosFisicos = psutil.cpu_count(logical=False)
nucleosLogicos = psutil.cpu_count(logical=True)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for item in Particoes:
    qtdParticoes += 1

print(f"Swap total: {swapTotal}")
print(f"Ram total: {ramTotal}")
print(f"Quantidade de CPUs: {nucleosFisicos}")
print(f"Quantidade de núcleos: {nucleosLogicos}")
print(f"Quantidade de partições: {qtdParticoes}")

for particao in Particoes:
    contador = 1
    contador + 1
    total  = round(psutil.disk_usage("/").total / (1024**3),2)  
    print(f"QUantidade total da partição {contador}: {total}")
    
for particao in Particoes:
    usoDisco = psutil.disk_usage(particao.mountpoint)
    print(particao.device)
    print(particao.fstype)
    print(particao.mountpoint)
    print(particao.opts)
    print(round(usoDisco.total / (1024**3),2))

dados = {
    "Swap total ": swapTotal,
    "Ram total": ramTotal,
    "Quantidade de CPUs ": nucleosFisicos,
    "Quantidade de núcleos lógicos": nucleosLogicos,
    "Capacidade total do disco": discoTotal,
    "Quantidade de partições do disco": qtdParticoes,
    "Data e hora da captura": timestamp
}


data.append(dados)


df1 = pd.DataFrame(data = data)

df1.to_csv('EspecificacoesHardware.csv',sep=';')

print("------- HARDWARE CAPTURADO -------")
