# -*- coding: utf-8 -*-
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config


def train_nlu():
    training_data = load_data("config/nlu_data.md")
    trainer = Trainer(config.load("config/nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist(path='./models',
                                      project_name='dbot',
                                      fixed_model_name='nlu')
    return model_directory


if __name__ == "__main__":
    train_nlu()
    print "train nlu done."
