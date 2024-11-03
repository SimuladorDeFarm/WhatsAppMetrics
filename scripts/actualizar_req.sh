#! /bin/bash

cd ..
rm requirements.txt
pip freeze > requirements.txt
echo "requirements.txt actualizado"
