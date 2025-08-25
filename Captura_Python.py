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
