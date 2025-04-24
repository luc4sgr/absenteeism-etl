"""
Implementação de Extractor para arquivos Excel (.xlsx).

Referências:
- pandas.read_excel
- glob.glob para leitura em lote
"""

import glob
import os
import pandas as pd

from app.core.interfaces.extractor import Extractor


class ExcelExtractor(Extractor):
    """
    Extrator de arquivos Excel a partir de um diretório.

    O fluxo de funcionamento é:
    1. Inicializamos com o caminho da pasta de entrada
    2. Localizamos todos os arquivos .xlsx
    3. Lemos cada um com pandas.read_excel()
    4. Retornamos uma lista de DataFrames
    """

    def __init__(self, input_folder: str):
        self.input_folder = input_folder

    def extract(self) -> list[pd.DataFrame]:
        # Lista todos os arquivos .xlsx da pasta
        pattern = os.path.join(self.input_folder, "*.xlsx")
        files = glob.glob(pattern)

        if not files:
            raise ValueError("Nenhum arquivo Excel encontrado no diretório informado.")

        # Lê cada arquivo usando pandas
        dataframes = [pd.read_excel(file) for file in files]
        return dataframes
