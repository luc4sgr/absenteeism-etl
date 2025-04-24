"""
Script para gerar dados de entrada sintéticos e rodar o pipeline ETL.

Executa:
1. Geração de n arquivos Excel falsos
2. Execução do pipeline ETL completo
"""

import os
from app.pipeline.etl_pipeline import ETLPipeline
from app.utils.absenteeism_generator import generate_absenteeism_data


def generate_excel_files(n: int = 10, path: str = "data/input"):
    """
    Gera arquivos Excel sintéticos para simular entrada do ETL.

    Args:
        n (int): Quantidade de arquivos a gerar.
        path (str): Caminho da pasta de saída.
    """
    os.makedirs(path, exist_ok=True)

    for i in range(n):
        df = generate_absenteeism_data()
        file_name = f"absenteeism_data_{i}.xlsx"
        df.to_excel(os.path.join(path, file_name), index=False)

    print(f"📁 {n} arquivos criados em {path}")


def run_pipeline():
    """
    Executa o pipeline ETL com os arquivos gerados.
    """
    pipeline = ETLPipeline(
        input_folder="data/input",
        output_folder="data/output",
        output_file_name="consolidated_absenteeism_data.xlsx"
    )
    pipeline.run()


if __name__ == "__main__":
    generate_excel_files(50)
    run_pipeline()
