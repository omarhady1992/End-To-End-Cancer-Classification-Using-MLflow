from src.Chest_Cancer_Classification.constants import *
from src.Chest_Cancer_Classification.utils.common import create_directories, read_yaml
from src.Chest_Cancer_Classification.entity.config_entity import TrainingConfig
from tensorflow.keras.optimizers import SGD
import tensorflow as  tf


class Training:
    def __init__(self, config:TrainingConfig):
        self.config =  config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_model_path)

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentated:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )


    def create_optimizer(self):

        SGD_Optimizer = SGD(learning_rate=self.config.params_learning_rate)
        return SGD_Optimizer


    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
        SGD_Optimizer = self.create_optimizer()


        self.model.compile(
            optimizer=SGD_Optimizer,
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

    @staticmethod
    def save_model(path:Path, model: tf.keras.Model):
        model.save(path)


