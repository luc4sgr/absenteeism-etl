"""
Testes unitários para o transformador padrão (DefaultTransformer).
"""

import pandas as pd
import pytest

from app.transformers.default_transformer import DefaultTransformer


@pytest.fixture
def sample_data():
    """
    Gera dois DataFrames com estrutura compatível para teste de concatenação.
    """
    df1 = pd.DataFrame({"ID": [1, 2], "Nome": ["Alice", "Bob"]})
    df2 = pd.DataFrame({"ID": [3, 4], "Nome": ["Carol", "Dave"]})
    return [df1, df2]


def test_transform_concats_dataframes(sample_data):
    # Arrange
    transformer = DefaultTransformer()

    # Act
    result = transformer.transform(sample_data)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (4, 2)
    assert list(result["Nome"]) == ["Alice", "Bob", "Carol", "Dave"]


def test_transform_raises_on_empty_input():
    # Arrange
    transformer = DefaultTransformer()

    # Act + Assert
    with pytest.raises(ValueError, match="Nenhum dado fornecido"):
        transformer.transform([])
