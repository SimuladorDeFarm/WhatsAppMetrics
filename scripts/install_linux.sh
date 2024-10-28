#! /bin/bash

#crea entorno virtual
echo "Creando entorno vitual..."
python -m venv venv

#activa el entorno vitual
source venv/bin/activate
echo "Entorno vitual ACTIVADO"

#instala las librerias de requeriments.txt
python -m pip install -r requirements.txt

#imprime las librerias
pip freeze 

#desactiva el entorno vitual
deactivate
echo "Entorno vitual DESACTIVADO"