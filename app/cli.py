"""
Interface de linha de comando (CLI) para o projeto ETL.

Executa comandos como:
- etl run --input data/input ...
- etl generate-data --count 50
"""

import typer
from app.pipeline.etl_pipeline import ETLPipeline
from app.utils.absenteeism_generator import generate_absenteeism_data
import os

app = typer.Typer()


@app.command()
def run(input: str, output: str, file: str):
    """
    Executa o pipeline ETL com os arquivos de entrada.
    """
    pipeline = ETLPipeline(input_folder=input, output_folder=output, output_file_name=file)
    pipeline.run()


@app.command()
def generate_data(count: int = 10, folder: str = "data/input"):
    """
    Gera arquivos Excel com dados fictícios de absenteísmo.
    """
    os.makedirs(folder, exist_ok=True)

    for i in range(count):
        df = generate_absenteeism_data()
        df.to_excel(os.path.join(folder, f"absenteeism_{i}.xlsx"), index=False)

    typer.echo(f"✅ Gerados {count} arquivos em {folder}")


if __name__ == "__main__":
    app()
