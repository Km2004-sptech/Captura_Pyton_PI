import psutil
import platform
import time
import csv
from datetime import datetime
import numpy as np

ARQUIVO = "dados_gerais.csv"
ARQUIVO2 = "captura_dados.csv"

# Cria arquivo com cabeçalho dos dados gerais do servidor (só na primeira vez)
try:
    with open(ARQUIVO, "x", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow(["nomeDoSO", "RealeaseDoSO", "VersãoDoSO", "Processador", "NúcleosFísicos", "NúcleosLógicos"])
except FileExistsError:
    pass

# Cria arquivo com cabeçalho dos dados do hardware (só na primeira vez)
try:
    with open(ARQUIVO2, "x", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow(["timestamp", "cpu", "ramTotal", "ramUsada", "discoTotal", "discoUsado"])
except FileExistsError:
    pass

# Informações do SO

nomeSo = platform.system()
realeaseSo = platform.release()
versaoSO = platform.version()
processador = platform.processor()
nucleosFisicos = psutil.cpu_count(logical=False)
nucleosLogicos = psutil.cpu_count(logical=True)

with open(ARQUIVO, "a", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow([nomeSo, realeaseSo, versaoSO, processador, nucleosFisicos, nucleosLogicos])

valores_cpu = []
tempos = []
t = 0

print("\n")
print("\n=== Iniciando Captura Contínua ===")
try:
    while True:
        uso = psutil.cpu_percent(interval=1) 
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ramTotal = round(psutil.virtual_memory().total / (1024**3),2)
        ramUsada = psutil.virtual_memory().percent
        discoTotal = round(psutil.disk_usage("/").total / (1024**3),2)
        discoUsado = psutil.disk_usage("/").percent

        valores_cpu.append(uso)
        tempos.append(t)


        if len(valores_cpu) > 0:
            print(f"{timestamp} | CPU: {uso}% | Ram total: {ramTotal}GB | Ram em Uso: {ramUsada}% | Disco total: {discoTotal}GB | Disco em uso: {discoUsado}%")


        with open(ARQUIVO2, "a", newline="") as f:
            writer = csv.writer(f, delimiter="|")
            writer.writerow([timestamp, uso, ramTotal, ramUsada, discoTotal, discoUsado])

        time.sleep(10)
        t += 10

except KeyboardInterrupt:#(Ctrl + c)
    print("\n=== Captura finalizada ===")