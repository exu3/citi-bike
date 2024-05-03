#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

# check if python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}python3 not installed. it's required for running this script${NC}"
    exit 1
fi

python3 -m venv citibike
echo -e "${GREEN}created virtual environment.${NC}"

. ./citibike/bin/activate
echo -e "${GREEN}activated virtual environment.${NC}"

echo -e "${GREEN}installing dependencies${NC}"
pip install -r requirements.txt

echo -e "${GREEN}generating maps...${NC}"
python maps.py

echo -e "${GREEN}generating graphs...${NC}"
python graphs.py

echo -e "${GREEN}starting the dev server...${NC}"
flask run
