import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import csv

CAPTURA_CSV = "captura_dados.csv"
DADOS_CSV = "dados_gerais.csv"

df = pd.read_csv(CAPTURA_CSV, sep="|", parse_dates=["timestamp"])

dfDados = pd.read_csv(DADOS_CSV, sep="|")

while True:
    print("\n=== Análise de Monitoramento ===")
    print("1. Informações do Sistema")
    print("2. Uso médio de RAM da última hora")
    print("3. Pico de uso de CPU em período")
    print("4. Média de uso de Disco nas últimas N horas")
    print("5. Carga total acumulada da CPU ao longo do tempo")
    print("6. Média temporal do uso de CPU")
    print("0. Sair")
    opcao = input("Escolha: ")



    if opcao == "1":
        print("\n=== Informações do Sistema ===\n")
        sistema = dfDados.iloc[0]
        sistema2 = df.iloc[0]
        print(f"Sistema Operacional: {sistema['nomeDoSO']} {sistema['RealeaseDoSO']}")
        print(f"Versão: {sistema['VersãoDoSO']}")
        print(f"Processador: {sistema['Processador']}")
        print(f"Núcleos Físicos: {sistema['NúcleosFísicos']}")
        print(f"Núcleos Lógicos (virtuais): {sistema['NúcleosLógicos']}")
        print(f"Ram total: {sistema2['ramTotal']}  Ram Usada: {sistema2['ramUsada']}%")
        print(f"Disco Total: {sistema2['discoTotal']}  Disco Usado: {sistema2['discoUsado']}%")


    elif opcao == "2":
        limite = datetime.now() - timedelta(hours=1)
        ultimos = df[df["timestamp"] >= limite]
        print(f"Média RAM última hora: {ultimos['ramUsada'].mean():.2f}%" if not ultimos.empty else "Sem dados suficientes.")
    
    elif opcao == "3":
        inicio = input("Início (AAAA-MM-DD HH:MM:SS): ")
        fim = input("Fim (AAAA-MM-DD HH:MM:SS): ")
        try:
            dt_inicio = pd.to_datetime(inicio)
            dt_fim = pd.to_datetime(fim)
            periodo = df[(df["timestamp"] >= dt_inicio) & (df["timestamp"] <= dt_fim)]
            print(f"Pico CPU no período: {periodo['cpu'].max():.2f}%" if not periodo.empty else "Sem dados no período.")
        except:
            print("Formato inválido.")
    
    elif opcao == "4":
        try:
            horas = int(input("Quantas horas? "))
            limite = datetime.now() - timedelta(hours=horas)
            ultimos = df[df["timestamp"] >= limite]

            if ultimos.empty:
                print("Sem dados suficientes.")
            else:
                uso_inicial = ultimos.iloc[0]['discoUsado']
                uso_final = ultimos.iloc[-1]['discoUsado']
                diferenca = uso_final - uso_inicial

                print(f"Média Disco últimas {horas} horas: {ultimos['discoUsado'].mean():.2f}%")
                print(f"Aumento no uso do Disco no período: {diferenca:.2f}%")
        except:
            print("Valor inválido.")


    elif opcao == "5":
        tempos = df["timestamp"].view('int64') / 1e9  # converter para segundos
        valores_cpu = df["cpu"]
        integral = round(np.trapz(valores_cpu, tempos), 2)
        print(f"Carga total acumulada da CPU: {integral}")

    elif opcao == "6":
        tempos = df["timestamp"].view('int64') / 1e9
        valores_cpu = df["cpu"]
        integral = np.trapz(valores_cpu, tempos)
        duracao = tempos.iloc[-1] - tempos.iloc[0]
        media_integral = round(integral / duracao, 2) if duracao != 0 else 0
        print(f"Média temporal do uso de CPU: {media_integral}%")
    
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")

        
