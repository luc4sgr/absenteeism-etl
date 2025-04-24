"""
Transformador padrão que consolida os dados extraídos de vários arquivos.

Referência:
- pandas.concat para união vertical de DataFrames
"""

import pandas as pd
from app.core.interfaces.transformer import Transformer


class DefaultTransformer(Transformer):
    """
    Implementação padrão de transformação.

    O fluxo de funcionamento é:
    1. Recebe uma lista de DataFrames extraídos
    2. Realiza concatenação vertical (append)
    3. Retorna um único DataFrame unificado

    Este transformador assume que todos os DataFrames possuem o mesmo schema.
    """

    def transform(self, data: list[pd.DataFrame]) -> pd.DataFrame:
        if not data:
            raise ValueError("Nenhum dado fornencido para transformação")

        # axis | Ação | Resultado
        # 0 | Concatenação vertical | Adiciona linhas
        # 1 | Concatenação horizontal | Adiciona colunas
        consolidated = pd.concat(data, axis=0, ignore_index=True)
        return consolidated
