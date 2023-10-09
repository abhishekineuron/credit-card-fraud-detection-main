from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
import logging

class TrainingPipeline:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.raw_data_dir = None
        self.train_arr = None
        self.test_arr = None
        self.preprocessor_path = None
        self.model_score = None

    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion()
            self.raw_data_dir = data_ingestion.initiate_data_ingestion()
        except Exception as e:
            self.logger.error("Data ingestion failed: %s", str(e))

    def start_data_transformation(self):
        try:
            data_transformation = DataTransformation(raw_data_dir=self.raw_data_dir)
            self.train_arr, self.test_arr, self.preprocessor_path = data_transformation.initiate_data_transformation()
        except Exception as e:
            self.logger.error("Data transformation failed: %s", str(e))

    def start_model_training(self):
        try:
            model_trainer = ModelTrainer()
            self.model_score = model_trainer.initiate_model_trainer(self.train_arr, self.test_arr, self.preprocessor_path)
        except Exception as e:
            self.logger.error("Model training failed: %s", str(e))

    def run_pipeline(self):
        try:
            self.start_data_ingestion()
            self.start_data_transformation()
            self.start_model_training()
            self.logger.info("Training completed. Trained model score: %s", self.model_score)
        except Exception as e:
            self.logger.error("Pipeline execution failed: %s", str(e))
