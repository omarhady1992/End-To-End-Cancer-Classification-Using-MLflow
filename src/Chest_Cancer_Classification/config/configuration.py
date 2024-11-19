from Chest_Cancer_Classification.constants import *
from Chest_Cancer_Classification.utils.common import create_directories, read_yaml
from Chest_Cancer_Classification.entity.config_entity import DataIngestionConfiguration, BaseModelConfig


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