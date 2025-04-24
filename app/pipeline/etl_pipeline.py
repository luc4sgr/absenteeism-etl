"""
Módulo orquestrador do processo ETL completo.

Este pipeline aplica:
1. Extração com ExcelExtractor
2. Transformação com DefaultTransformer
3. Carga com ExcelLoader
"""

from app.extractors.excel_extractor import ExcelExtractor
from app.transformers.default_transformer import DefaultTransformer
from app.loaders.excel_loader import ExcelLoader
from app.core.logger import get_logger

class ETLPipeline:
    """
    Classe que coordena os passos do ETL.

    O fluxo de funcionamento é:
    1. Instancia os componentes com base nos paths fornecidos
    2. Executa extract → transform → load
    """
    
    def __init__(self, input_folder:str, output_folder:str, output_file_name:str):
        self.extractor = ExcelExtractor(input_folder)
        self.transformer = DefaultTransformer()
        self.loader = ExcelLoader(output_folder, output_file_name)
        self.logger = get_logger("ETLPipeline")
    
    def run(self):
        """
        Executa o pipeline completo de ETL.
        """
        self.logger.info("Iniciando processo ETL")
        self.logger.info("🔍 Extraindo arquivos...")
        raw_data = self.extractor.extract()
        
        self.logger.info("🔧 Transformando dados...")
        consolidated = self.transformer.transform(raw_data)
        
        
        self.logger.info("📦 Salvando arquivo final...")
        self.loader.load(consolidated)

        self.logger.info("✅ ETL finalizado com sucesso.")