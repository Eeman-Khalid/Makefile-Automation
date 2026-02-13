setup:
	py -3.13 -m pip install --upgrade pip
	py -3.13 -m pip install -r requirements.txt

download-data:
	py -3.13 scripts/download_data.py

preprocess: download-data
	py -3.13 scripts/preprocess.py

features: preprocess
	py -3.13 scripts/feature_engineering.py

train: features
	py -3.13 scripts/train_model.py

predict: train
	py -3.13 scripts/predict.py

evaluate: predict
	py -3.13 scripts/evaluate.py

all: setup train evaluate
