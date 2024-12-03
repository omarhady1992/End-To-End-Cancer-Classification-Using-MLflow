import os
from src.Chest_Cancer_Classification.constants import *
from src.Chest_Cancer_Classification.utils.common import create_directories, read_yaml
from src.Chest_Cancer_Classification.entity.config_entity import DataIngestionConfiguration, BaseModelConfig, TrainingConfig, EvaluationConfig


class ConfigurationManager:
    '''
    General Configuration class containing configuration methods for every component
    '''
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion(self)-> DataIngestionConfiguration:

        '''
        Method for adding configurations to data ingesting component
        '''
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfiguration(
            root_dir=config.root_dir,
            source_url= config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    

    def get_base_model(self)-> BaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        base_model_config = BaseModelConfig(
            root_dir = config.root_dir,
            base_model_path = config.base_model_path,
            updated_base_model_path = config.updated_base_model_path,
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top= self.params.INCLUDE_TOP,
            params_weight= self.params.WEIGHTS,
            params_classes= self.params.CLASSES)
        return base_model_config
    
    def training_model_config(self)->TrainingConfig:
        training= self.config.training
        base_model = self.config.prepare_base_model
        params = self.params
        data = os.path.join(self.config.data_ingestion.unzip_dir, 'Chest-CT-Scan-data')

        training_config = TrainingConfig(

            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_model_path=Path(base_model.updated_base_model_path),
            training_data=Path(data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentated=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE)
        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/Chest-CT-Scan-data",
            mlflow_uri="https://dagshub.com/omarhady1992/End-To-End-Cancer-Classification-Using-MLflow.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE,
            params_learning_rate = self.params.LEARNING_RATE
        )
        return eval_config