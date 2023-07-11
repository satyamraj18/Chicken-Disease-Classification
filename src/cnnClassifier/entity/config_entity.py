from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)        #Its an entity as it will help to create your own custom return type
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:   #It will take the path from the config.yaml's "prepare_base_model" and other values are obtained from
    root_dir: Path              #params.yaml which includes the parameters being used for the base model
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int