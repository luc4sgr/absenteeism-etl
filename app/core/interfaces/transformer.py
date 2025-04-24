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


class Transformer(ABC):
    """
    Interface base para qualquer componente de transformação de dados.

    O fluxo de funcionamento é:
    1. Recebe uma lista de DataFrames extraídos
    2. Aplica transformações específicas (merge, limpeza, cálculo)
    3. Retorna um único DataFrame consolidado
    """

    @abstractmethod
    def transform(self, data: list[pd.DataFrame]) -> pd.DataFrame:
        pass

