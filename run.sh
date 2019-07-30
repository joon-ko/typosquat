#!/bin/bash
set -ex

# create/start venv
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run app
export FLASK_APP=typosquat/app.py
flask run
