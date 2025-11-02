from pathlib import Path
import pandas as pd
import numpy as np
import sys

class LeitorPlanilha:#
    #classe p ler e processar planilhas de autômatos
    
    
    def __init__(self):
        #método construtor
        self.base = Path(__file__).resolve().parent.parent
    
    def localizar_planilha(self, nome_arquivo: str) -> Path:
        #localiza arquivos com pathlib
        caminho = self.base / "tests" / "fixtures" / "planilhas" / nome_arquivo
        return caminho
    
    def ler_planilha(self, nome_arquivo: str) -> pd.DataFrame:
        #método q lê a planilha usando pandas
        caminho = self.localizar_planilha(nome_arquivo)
        
        if not caminho.exists():
            raise FileNotFoundError(f"Planilha não encontrada na Pasta: {caminho}")
        
        #tratamento de formato CSV ou Excel
        if nome_arquivo.endswith('.csv'):
            df = pd.read_csv(caminho, sep=";")
        elif nome_arquivo.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(caminho)
        else:
            raise ValueError(f"Formato não suportado: {nome_arquivo}")
            
        return df
    
    def extrair_automato(self, nome_arquivo: str) -> dict:
        #método que extrai as transições e gera um dicionário
        
        try: #tenta extrair os dados e gerar o dicionário
            dicionario_automato = {}
            df = self.ler_planilha(nome_arquivo)

            print("PLANILHA CARREGADA:", nome_arquivo)
        
            for idx, row in df.iterrows():
                estado = row[df.columns[0]]
                dicionario_automato[estado] = row[1:].to_dict()

            return dicionario_automato
             
        except FileNotFoundError as e: #tratando possíveis erros de tentativas falhas
            print("ERRO:", e)
            print("CWD ATUAL:", Path.cwd())
            raise
        except Exception as e:
            print("ERRO INESPERADO:", e)
            raise

if __name__ == "__main__":
    leitor = LeitorPlanilha()
    arquivo = input("Digite o Nome da Planilha:\n")
    
    try:
        automato = leitor.extrair_automato(arquivo)
    except Exception as e:
        print(f"Erro ao processar: {e}")
        sys.exit(1)