#! /bin/bash

#sys.prefix != sys.base_prefix
#if diff sys.prefix sys.base_prefix >/dev/null;
#then 
#    echo "estas en el entorno virtual"
#fi

source venv/bin/activate
python main.py
deactivate