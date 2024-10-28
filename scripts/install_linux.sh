#! /bin/bash

#create virtual enviroment
echo "Creating virtual enviroment..."
python -m venv venv

#activate virtual enviroment
source venv/bin/activate
echo "Virtual enviroment ACTIVATED"

#Install the libreries of requirements.txt
echo "Installing libraries"
python -m pip install -r requirements.txt

#print install process
pip freeze 

#deactivate virtual enviroment
deactivate
echo "Virtual Enviroment DEACTIVATE"