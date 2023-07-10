from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,       #Will get this value from constants folder you have
        params_filepath = PARAMS_FILE_PATH):      #Will get this value from constants folder you have

        self.config = read_yaml(config_filepath)      #Calling the read_yaml method which we have defined in the common.py in utils folder
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])  #artifacts roots is the key defined in the config.yaml


    
    def get_data_ingestion_config(self) -> DataIngestionConfig: #Return type will be an entity defined above
        config = self.config.data_ingestion   #This will store data ingestion key which 4 other key in it. You can see the same in config.yaml
        #As the return type of the read_yaml is config box so we can access key using "."

        create_directories([config.root_dir])   

        data_ingestion_config = DataIngestionConfig(         #Using the entity you have created above
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config