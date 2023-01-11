from dataclasses import dataclass
import os
from s3_syncer import S3Sync
from constant import *


@dataclass
class ModelServingConfig:
    s3_mar_file_path: str = S3_MAR_FILE_URI
    model_store_path: str = os.path.join(ROOT, MODEL_STORE)
    mar_file_path: str = os.path.join(model_store_path, MAR_FILE_NAME)


class Serving:
    def __init__(self, model_serving_config: ModelServingConfig):
        self.model_serving_config = model_serving_config
        self.s3_sync = S3Sync()


    def get_mar_from_s3(self):
        print(f"creating directory>>>>> at {self.model_serving_config.model_store_path}")
        os.makedirs(self.model_serving_config.model_store_path, exist_ok= True)
        self.s3_sync.sync_folder_from_s3(folder=self.model_serving_config.model_store_path,
                    aws_bucket_url=self.model_serving_config.s3_mar_file_path)
        print(self.model_serving_config.mar_file_path)
        print(os.path.isfile(self.model_serving_config.mar_file_path))

    def serve_model(self):
        os.system(f"torchserve --start --model-store {self.model_serving_config.model_store_path} --models model={MAR_FILE_NAME} --ts-config config.properties")

    def initiate_serving(self):
        print(self.model_serving_config.model_store_path)
        print(self.model_serving_config.s3_mar_file_path)
        print(ROOT)
        self.get_mar_from_s3()
        self.serve_model()


if __name__ == '__main__':
    model_serving_config = ModelServingConfig()
    serving = Serving(model_serving_config)
    serving.initiate_serving()