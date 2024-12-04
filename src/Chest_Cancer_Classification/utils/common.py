#frequently imported modules
import os
from box.exceptions import BoxValueError
import yaml
from src.Chest_Cancer_Classification import logger
import json
from ensure import ensure_annotations
import joblib
import base64
from typing import Any
from box import ConfigBox
from pathlib import Path



@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:

    """
    Args:
        path(str): path-like input for yaml file

    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type

    """

    try:
        with open(path) as y_file:
            content = yaml.safe_load(y_file)
            logger.info(f"{path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def load_jason(path: Path)-> ConfigBox:
    '''
    a function that loads .json files 

    Args: 
        path: a path-like input to the .json file location
    Returns
        ConfigBox: data as class attributes not dictionary
    '''

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file {path} loaded")
    return ConfigBox(content)

@ensure_annotations
def save_jason(path: Path, data: dict):
    '''
    a function that loads .json files 

    Args: 
        path: a path-like input to the .json file location
        data (dictionary):
    '''

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"saved json data in json file {path}")

@ensure_annotations
def save_bin(data: Any, path:Path):
    '''save binary files

    Args:
    data (any): data to be saved
    path (str): path to binary file for saving data

    '''
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved successfully in {path}")

@ensure_annotations
def load_jason(path: Path)-> Any:
    '''
    a function that loads .bin files 

    Args: 
        path: a path-like input to the .json file location
    Returns
       data
    '''

    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path)->str:
    '''
    a function that returns the size of an input file
    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    '''
    sizeinkb = round(os.path.getsize(path)/1024)
    return f"{sizeinkb} KB"

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())