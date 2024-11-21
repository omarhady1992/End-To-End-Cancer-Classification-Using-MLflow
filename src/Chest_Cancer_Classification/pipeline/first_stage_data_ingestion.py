from src.Chest_Cancer_Classification.config.configuration import ConfigurationManager
from src.Chest_Cancer_Classification.components.data_ingestion import DataIngest
from src.Chest_Cancer_Classification import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configuration = ConfigurationManager()
        data_config = configuration.get_data_ingestion()
        data_ingestion = DataIngest(config=data_config)
        data_ingestion.download_data_googledrive()
        data_ingestion.unzip_data()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e