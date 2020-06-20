#!/bin/bash

python -m rasa_core.run --enable_api --port 5005 -d models/dialogue -u dbot/nlu -o logs/rasa_core.log --endpoints config/endpoints.yml --credentials config/credentials.yml
