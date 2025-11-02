#código da classe leitor
from pathlib import Path #p encontrar o caminho de forma robusta
import pandas as pd #leitura arquivo excel
import numpy as np #lib 
import sys #pra conseguir me situar nos diterórios do sistema

def localizar_planilha(nome_arquivo: str) -> Path: #localiza arquivos com pathlib de forma robusta

    base = Path(__file__).resolve().parent.parent #o método .parent é p subir um nível no diretório facilitando p encontro do path
    
    caminho = base / "tests" / "fixtures" / "planilhas" / nome_arquivo #montando o caminho das planilhas
    
    return caminho

def ler_planilha(nome_arquivo: str): #funçao q le a planilha usando pandas

    caminho = localizar_planilha(nome_arquivo) #chama a função que localiza o arquivo
    
    if not caminho.exists(): #verifica se o arquivo existe por meio do caminho

        raise FileNotFoundError(f"Planilha não encontrada na Pasta: {caminho}")
    
    df = pd.read_csv(caminho)  #lê o arquivo excel (.xlsx) usando pandas
    return df

if __name__ == "__main__": #classe principal para rodar o projeto

    arquivo = input("Digite o Nome da Planilha:\n") #lê nome da planilha
    
    try: #bloco q tenta realizar a leitura
        
        df = ler_planilha(arquivo) #lê a planilha

        print("PLANILHA CARREGADA:", arquivo)
        
        print("DIMENSÃO (LINHAS, COLUNAS):", df.shape) #df.shape é uma tupla (linhas, colunas)

        print(df.head()) #mostra 5 primeiras linhas

        print("COLUNAS: ", df.columns) #colunas

        print("INFORMAÇÃO: ", df.info())
        
        

    except FileNotFoundError as e: #exceção aponta caminho atual caso a leitura não dê certo
        
        print("ERRO:", e)
        
        print("CWD ATUAL:", Path.cwd())
        
        sys.exit(1)
    
    except Exception as e: 
        print("ERRO INESPERADO:", e)
        sys.exit(2)
