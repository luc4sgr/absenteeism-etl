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
def run(
    tipo: str = typer.Option(..., "--tipo", "-t", help="Tipo de dado: despesas, ausencias, etc."),
    file: str = typer.Option(..., "--file", "-f", help="Nome do arquivo final (.xlsx)"),
):
    """
    Executa o pipeline ETL para um determinado tipo de dado.

    As pastas de entrada/saída são fixas:
    - Entrada: data/input/{tipo}/
    - Saída:  data/output/{tipo}/
    """
    input_folder = f"data/input/{tipo}"
    output_folder = f"data/output/{tipo}"

    pipeline = ETLPipeline(
        input_folder=input_folder,
        output_folder=output_folder,
        output_file_name=file
    )
    pipeline.run()



@app.command()
def generate_data(
    tipo: str = typer.Option(..., "--tipo", "-t", help="Tipo de dado a gerar"),
    count: int = typer.Option(10, "--count", "-c", help="Quantidade de arquivos"),
):
    """
    Gera arquivos Excel sintéticos para simular dados do ETL.
    """
    folder = f"data/input/{tipo}"
    os.makedirs(folder, exist_ok=True)

    for i in range(count):
        df = generate_absenteeism_data()
        df.to_excel(os.path.join(folder, f"{tipo}_{i}.xlsx"), index=False)

    typer.echo(f"✅ Gerados {count} arquivos em {folder}")



if __name__ == "__main__":
    app()
