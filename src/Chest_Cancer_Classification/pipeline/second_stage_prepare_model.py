from src.Chest_Cancer_Classification.config.configuration import ConfigurationManager
from src.Chest_Cancer_Classification.components.base_model import BaseModel
from src.Chest_Cancer_Classification import logger



STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_base_model()
        prepare_base_model = BaseModel(config=prepare_base_model_config)
        prepare_base_model.create_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e