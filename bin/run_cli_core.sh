#!/bin/bash

python -m rasa_core.run -d models/dialogue -u models/dbot/nlu -o logs/rasa.log
