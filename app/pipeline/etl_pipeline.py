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
    
    def run(self):
        """
        Executa o pipeline completo de ETL.
        """
        print("🔍 Extraindo arquivos...")
        
        raw_data = self.extractor.extract()
        
        print("🔧 Transformando dados...")
        consolidated = self.transformer.transform(raw_data)
        
        
        print("📦 Salvando arquivo final...")
        self.loader.load(consolidated)

        print("✅ ETL finalizado com sucesso.")