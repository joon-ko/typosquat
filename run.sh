#!/bin/bash
set -ex

# create/start venv
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# required as a fix for an obscure fork() bug
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

# run app
export FLASK_APP=typosquat/app.py
flask run
