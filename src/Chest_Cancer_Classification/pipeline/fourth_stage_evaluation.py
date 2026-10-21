from src.Chest_Cancer_Classification.config.configuration import ConfigurationManager
from src.Chest_Cancer_Classification.components.evaluation import Evaluation
from src.Chest_Cancer_Classification import logger
import os
from dotenv import load_dotenv

# DagsHub / MLflow credentials are read from the environment (or a local .env file).
# See .env.example for the variable names. Never hardcode credentials here.
load_dotenv()
os.environ.setdefault(
    "MLFLOW_TRACKING_URI",
    "https://dagshub.com/omarhady1992/End-To-End-Cancer-Classification-Using-MLflow.mlflow",
)

STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        for var in ("MLFLOW_TRACKING_USERNAME", "MLFLOW_TRACKING_PASSWORD"):
            if not os.environ.get(var):
                raise EnvironmentError(f"{var} is not set. Copy .env.example to .env and fill it in.")
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
            