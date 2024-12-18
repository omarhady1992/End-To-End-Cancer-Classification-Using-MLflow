from src.Chest_Cancer_Classification.config.configuration import ConfigurationManager
from src.Chest_Cancer_Classification.components.evaluation import Evaluation
from src.Chest_Cancer_Classification import logger
import os

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/omarhady1992/End-To-End-Cancer-Classification-Using-MLflow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="omarhady1992"
os.environ["MLFLOW_TRACKING_PASSWORD"]="Gagoal_123"

STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            