#create the data class
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfiguration:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path 

#Create data class for base model (update entity)
from dataclasses import dataclass
from pathlib import Path

@dataclass
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weight: str
    params_classes: int

@dataclass
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_model_path: Path
    training_data: Path
    params_learning_rate: float
    params_epochs: int
    params_batch_size: int
    params_is_augmentated: bool
    params_image_size: float

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int
    params_learning_rate: float