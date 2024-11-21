#Module for the data ingestion component of the process

import os
import zipfile
from src.Chest_Cancer_Classification.utils.common import get_size 
from src.Chest_Cancer_Classification import logger
from src.Chest_Cancer_Classification.entity.config_entity import DataIngestionConfiguration
import gdown

class DataIngest:
    def __init__(self, config:DataIngestionConfiguration):
        self.config = config

    def download_data_googledrive(self) -> str:
        ''' Get data from url'''

        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into {zip_download_dir}")
            print(dataset_url)
            file_id = dataset_url.split('/')[-2]
            gdrive_dl_prefix = 'https://drive.google.com/uc?/export=download&id='

            gdown.download(gdrive_dl_prefix+file_id, zip_download_dir)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e
        
    def unzip_data(self):
        '''Unpack Data'''
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)