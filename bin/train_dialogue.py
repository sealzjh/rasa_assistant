# -*- coding: utf-8 -*-
import sys
from rasa_core.train import train_dialogue_model


def train_dialogue(domain_file="config/domain.yml",
                   model_path="models/dialogue",
                   stories_file="config/stories.md",
                   policy_config="config/policy_config.yml"
                   ):
                   #endpoints_file="config/endpoints.yml"):

    train_dialogue_model(domain_file=domain_file,
                         stories_file=stories_file,
                         output_path=model_path,
                         policy_config=policy_config,
                         kwargs=_additional_arguments())


def _additional_arguments():
    additional = {
        "augmentation_factor": 50,
        "debug_plots": False
    }

    # remove None values
    return {k: v for k, v in additional.items() if v is not None}


if __name__ == '__main__':
    train_dialogue()
    print "train dialogue done."
