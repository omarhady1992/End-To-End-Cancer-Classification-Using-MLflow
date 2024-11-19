from src.Chest_Cancer_Classification import logger
from src.Chest_Cancer_Classification.pipeline.first_stage_data_ingestion import DataIngestionTrainingPipeline
from src.Chest_Cancer_Classification.pipeline.second_stage_prepare_model import PrepareBaseModelTrainingPipeline
from src.Chest_Cancer_Classification.pipeline.third_stage_training import TrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'Training'

try:
    logger.info(f" Starting {STAGE_NAME}")
    trainer = TrainingPipeline()
    trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e