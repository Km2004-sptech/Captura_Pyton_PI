import psutil
import platform
import time
import csv
import requests
from datetime import datetime
import numpy as np


ARQUIVO = "dados_gerais.csv"
ARQUIVO2 = "captura_dados.csv"
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

# Cria arquivo com cabeçalho dos dados gerais do servidor (só na primeira vez)
try:
    with open(ARQUIVO, "x", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow(["nomeMaquina", "nomeDoSO", "RealeaseDoSO", "VersãoDoSO", "Processador", "NúcleosFísicos", "NúcleosLógicos"])
except FileExistsError:
    pass

# Cria arquivo com cabeçalho dos dados do hardware 
try:
    with open(ARQUIVO2, "x", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow(["timestamp", "nomeMaquina", "cpu", "ramTotal", "ramUsada", "discoTotal", "discoUsado"])
except FileExistsError:
    pass

# Informações do SO

nomeSo = platform.system()
realeaseSo = platform.release()
versaoSO = platform.version()
processador = platform.processor()
nucleosFisicos = psutil.cpu_count(logical=False)
nucleosLogicos = psutil.cpu_count(logical=True)
nomeMaquina = platform.node()

with open(ARQUIVO, "a", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow([nomeMaquina, nomeSo, realeaseSo, versaoSO, processador, nucleosFisicos, nucleosLogicos])



# cria a função para enviar mensagem no canal de suporte usando o InfoMan
def enviar_mensagem_slack(menssagem):
    textoEnviado = {'text': menssagem}
    requests.post(SLACK_WEBHOOK_URL, json=textoEnviado)


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
        limiteCPU = 50

        print(f"{timestamp} | Nome da Máquina: {nomeMaquina} | CPU: {uso}% | Ram total: {ramTotal}GB | Ram em Uso: {ramUsada}% | Disco total: {discoTotal}GB | Disco em uso: {discoUsado}%")
       
        if uso > limiteCPU:
            enviar_mensagem_slack(f":warning: ALERTA NA MÁQUINA: Nome: {nomeMaquina} Uso de CPU acima de {limiteCPU}%! Atual: {uso}%")

         


        with open(ARQUIVO2, "a", newline="") as f:
            writer = csv.writer(f, delimiter="|")
            writer.writerow([timestamp, nomeMaquina, uso, ramTotal, ramUsada, discoTotal, discoUsado])

        time.sleep(10)

except KeyboardInterrupt:#(Ctrl + c)
    print("\n=== Captura finalizada ===")