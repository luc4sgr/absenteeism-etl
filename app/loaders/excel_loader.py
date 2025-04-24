"""
Loader que exporta os dados transformados para um arquivo Excel (.xlsx).

Referência:
- pandas.DataFrame.to_excel
- os.makedirs para criar pastas dinamicamente
"""
import os
import pandas as pd
from app.core.interfaces.loader import Loader

class ExcelLoader(Loader):
    """
    Implementação da interface Loader que salva dados em um arquivo Excel.

    O fluxo de funcionamento é:
    1. Recebe a pasta de saída e nome do arquivo
    2. Cria a pasta se ela não existir
    3. Salva o DataFrame consolidado com to_excel()

    type: df: pd.DataFrame
    """

    def __init__(self, output_folder: str, output_file_name: str):
        self.output_folder = output_folder
        self.output_file_name = output_file_name

    def load(self, df: pd.DataFrame):
        # Garante que a pasta de saída exista
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        # Caminho completo do arquivo de saída
        full_path = os.path.join(self.output_folder, self.output_file_name)
         
        # Exporta o DataFrame para Excel
        df.to_excel(full_path, index=False)