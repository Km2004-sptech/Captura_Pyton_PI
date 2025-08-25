import psutil
import platform
import time
import csv
from datetime import datetime
import numpy as np

ARQUIVO = "captura_dados.csv"

# Cria arquivo com cabeçalho (só na primeira vez)
try:
    with open(ARQUIVO, "x", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow(["timestamp", "usuariosLogados", "cpu", "ramTotal", "ramUsada", "discoTotal", "discoUsado", "integral_acumuladada", "média_integral"])
except FileExistsError:
    pass

# Informações do SO
print("=== Informações do Sistema ===")
print(f"Sistema Operacional: {platform.system()} {platform.release()}")
print(f"Versão: {platform.version()}")
print(f"Processador: {platform.processor()}")
print(f"Núcleos Físicos: {psutil.cpu_count(logical=False)}")
print(f"Núcleos Lógicos (virtuais): {psutil.cpu_count(logical=True)}")

valores_cpu = []
tempos = []
t = 0

print("\n")
print("\n=== Iniciando Captura Contínua ===")

try:
    while True:
        usuariosLogados = len(psutil.users())
        uso = psutil.cpu_percent(interval=1) # mede CPU em % (uso_k)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ramTotal = round(psutil.virtual_memory().total / (1024**3),2)
        ramUsada = psutil.virtual_memory().percent
        discoTotal = round(psutil.disk_usage("/").total / (1024**3),2)
        discoUsado = psutil.disk_usage("/").percent
