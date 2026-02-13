Titanic Survival Prediction Automated Pipeline Using Makefile

Overview

This project demonstrates an end-to-end machine learning pipeline for predicting Titanic passenger survival. The pipeline is fully automated using GNU Make, ensuring reproducibility and easy execution.

Key features include:

Automated setup of dependencies

Downloading and preprocessing the Titanic dataset

Feature engineering

Model training using Random Forest

Generating predictions and evaluating performance

Clean, modular project structure

Project Structure
MLOPs Assignment-01/
├── data/
│   ├── raw/            # Raw Titanic dataset
│   └── processed/      # Preprocessed dataset
├── features/           # Engineered features
├── models/             # Trained ML models
├── results/            # Predictions and evaluation metrics
├── scripts/            # Python scripts for each stage
├── Makefile            # Automation controller
├── requirements.txt    # Python dependencies
└── README.md

Prerequisites

Python 3.13

GNU Make installed

Git (optional, for version control)

Makefile Targets
Target	Description
make setup	Installs Python dependencies from requirements.txt
make download-data	Downloads the Titanic dataset to data/raw/
make preprocess	Cleans and prepares the dataset, saves to data/processed/
make feature	Performs feature engineering, saves features to features/
make train	Trains a Random Forest model and saves it to models/
make predict	Generates predictions and saves results to results/
make evaluate	Calculates accuracy, precision, recall, and F1-score, saves to results/
make all	Runs the entire pipeline from setup to evaluation
make clean	Removes generated files and outputs
Usage

Clone the repository:

git clone https://github.com/Eeman-Khalid/Makefile-Automation.git
cd Makefile-Automation


Run the full pipeline:

make all


Or run stages individually:

make setup
make download-data
make preprocess
make feature
make train
make predict
make evaluate


Clean generated outputs (optional):

make clean

Outputs

Processed Dataset: data/processed/titanic_processed.csv

Features: features/titanic_features.csv

Model: models/random_forest.pkl

Predictions: results/predictions.csv

Evaluation Metrics: results/metrics.txt

Notes

All stages are automated via the Makefile; manual execution of scripts is discouraged.

The pipeline ensures reproducibility and modularity.

This project follows MLOps best practices for automation and version control.