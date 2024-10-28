#! /bin/bash

rm requirements.txt
pip freeze > requirements.txt
echo "requirements.txt actualizado"