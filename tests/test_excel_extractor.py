"""
Testes unitários para o ExcelExtractor.

Usa o padrão AAA:
- Arrange: preparar os dados
- Act: executar o método a ser testado
- Assert: verificar o resultado
"""

import os
import pandas as pd
import pytest

from app.extractors.excel_extractor import ExcelExtractor


@pytest.fixture
def temp_excel_files(tmp_path):
    """
    Cria dois arquivos Excel fictícios em uma pasta temporária.
    """
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

    file1 = tmp_path / "file1.xlsx"
    file2 = tmp_path / "file2.xlsx"

    df1.to_excel(file1, index=False)
    df2.to_excel(file2, index=False)

    return tmp_path

def test_extract_returns_dataframes(temp_excel_files):
    # Arrange
    extractor = ExcelExtractor(input_folder=str(temp_excel_files))

    # Act
    result = extractor.extract()

    # Assert
    assert isinstance(result, list)
    assert all(isinstance(df, pd.DataFrame) for df in result)
    assert len(result) == 2
    
def test_extract_raises_if_no_files(tmp_path):
    # Arrange
    extractor = ExcelExtractor(input_folder=str(tmp_path))

    # Act + Assert
    with pytest.raises(ValueError, match="Nenhum arquivo Excel encontrado"):
        extractor.extract()