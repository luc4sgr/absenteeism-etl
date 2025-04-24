"""
Testes unitários para o componente ExcelLoader.
"""

import pandas as pd

from app.loaders.excel_loader import ExcelLoader


def test_loader_creates_excel_file(tmp_path):
    # Arrange
    df = pd.DataFrame({
        "ID": [1, 2, 3],
        "Nome": ["Lucas", "Ana", "João"]
    })

    output_folder = tmp_path / "output"
    output_filename = "consolidado.xlsx"
    full_path = output_folder / output_filename

    loader = ExcelLoader(str(output_folder), output_filename)

    # Act
    loader.load(df)

    # Assert
    assert full_path.exists() is True

    # Valida o conteúdo do arquivo salvo
    loaded_df = pd.read_excel(full_path)
    pd.testing.assert_frame_equal(df, loaded_df)
