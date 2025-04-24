"""
Gera dados fictícios de absenteísmo para simulação de entrada do ETL.

Usa a biblioteca Faker com localização pt_BR para nomes e datas.
"""

import random
import pandas as pd
from faker import Faker


def generate_absenteeism_data(n: int = 10) -> pd.DataFrame:
    """
    Gera um DataFrame com n registros aleatórios de absenteísmo.

    Args:
        n (int): Quantidade de linhas no DataFrame gerado.

    Returns:
        pd.DataFrame: Dados fictícios com colunas realistas.
    """
    faker = Faker("pt_BR")

    departamentos = [
        "Recursos Humanos", "Financeiro", "Marketing", "TI", "Vendas",
        "Operações", "Jurídico", "Engenharia", "Atendimento", "P&D"
    ]
    motivos = ["Doença", "Problemas pessoais", "Consulta médica", "Viagem", "Outros"]

    data = {
        "Colaborador_id": [faker.unique.random_number(digits=5) for _ in range(n)],
        "Colaborador_nome": [faker.name() for _ in range(n)],
        "Departamento": [faker.random_element(departamentos) for _ in range(n)],
        "Motivo_da_ausência": [faker.random_element(motivos) for _ in range(n)],
        "Horas_de_ausência": [faker.random_int(min=1, max=8) for _ in range(n)],
        "Data_da_ausência": [
            faker.date_between(start_date="-60d", end_date="today") for _ in range(n)
        ],
        "Salário": [round(random.uniform(2500, 12500), 2) for _ in range(n)],
    }

    df = pd.DataFrame(data)
    df["Data_da_ausência"] = pd.to_datetime(df["Data_da_ausência"])

    return df
