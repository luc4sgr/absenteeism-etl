"""
Configuração centralizada de logging para o projeto.
"""

import logging


def get_logger(name: str = "ETL") -> logging.Logger:
    """
    Retorna um logger configurado com formato padrão.

    Args:
        name (str): Nome do logger (geralmente o módulo).

    Returns:
        logging.Logger
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        logger.addHandler(console)

    return logger
