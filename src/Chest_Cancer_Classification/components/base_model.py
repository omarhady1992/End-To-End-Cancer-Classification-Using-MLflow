import os
import zipfile
import tensorflow as tf
from pathlib import Path
from urllib import request
from src.Chest_Cancer_Classification.entity.config_entity import BaseModelConfig

class BaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config

    def create_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape = self.config.params_image_size,
            weights = self.config.params_weight,
            include_top = self.config.params_include_top

        )

        self.save_model(path= self.config.base_model_path, model=self.model)

    @staticmethod
    def save_model(path:Path, model: tf.keras.Model):
        return model.save(path)
    
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        ''' 
        A static method to create the full model using a base model from transfer learning

        Arguments:
            model (keras.Model object): base model
            classes: no. of classes that the model will classify
            freeze_all (bool): if True freezes all the layers of the base model without updating
            freeze_till (int) : if given, the number of layers that shouldn't be updated 
                                and the layers after it will be updated
            learning_rate (float): model learning rate for updating
        '''

        if freeze_all:
            for layers in model.layers:
                model.trainable = False
        elif (freeze_till is not None):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        predict_in = tf.keras.layers.Dense(units=classes, activation = "softmax")(flatten_in)

        full_model = tf.keras.models.Model(inputs=model.input, outputs=predict_in )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)