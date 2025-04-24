"""
Este módulo define as interfaces base para os componentes do processo ETL.

O objetivo é garantir o desacoplamento entre as implementações concretas
e a orquestração do pipeline.

Referências:
- Padrão Strategy (para transformadores)
- Princípios SOLID: Interface Segregation
"""

from abc import ABC, abstractmethod
import pandas as pd


class Extractor(ABC):
    """
    Interface base para qualquer componente de extração de dados.
    
    O fluxo de funcionamento é:
    1. Recebe como entrada uma origem de dados (ex: caminho de pasta)
    2. Realiza a leitura de arquivos ou conexão com fontes externas
    3. Retorna uma lista de DataFrames para processamento posterior
    """

    @abstractmethod
    def extract(self) -> list[pd.DataFrame]:
        pass
    
    
