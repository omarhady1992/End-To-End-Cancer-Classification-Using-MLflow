from src.Chest_Cancer_Classification.config.configuration import ConfigurationManager
from src.Chest_Cancer_Classification.components.training import Training
from src.Chest_Cancer_Classification import logger


STAGE_NAME = 'Training'

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configuration = ConfigurationManager()
        training_config = configuration.training_model_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f" Starting {STAGE_NAME}")
        trainer = TrainingPipeline()
        trainer.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e