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


class Loader(ABC):
    """
    Interface base para qualquer componente de carga dos dados.

    O fluxo de funcionamento é:
    1. Recebe um DataFrame consolidado
    2. Salva os dados em um destino (arquivo, banco de dados, API)
    3. Pode criar pastas ou conexões se necessário
    """

    @abstractmethod
    def load(self, df: pd.DataFrame):
        pass