#!bin/bash
python3 -m pipenv lock
python3 -m pipenv install -r requirements.txt
python3 -m pipenv srun python3 main.py
