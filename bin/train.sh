#!/bin/bash

python bin/train_nlu.py
python bin/train_dialogue.py

#python -m rasa_core.train -d config/domain.yml -s config/stories.md -o models/dialogue
#python -m rasa_nlu.train -c config/nlu_config.yml --data config/nlu_data.md -o models --fixed_model_name nlu --project dbot --verbose
