# Honkai Star Rail Map Classifier

A CNN model that classifies game map areas from Honkai Star Rail into three categories: Herta Space Station, Jarilo-VI, and The Luofu.

## Features
- Custom CNN model trained from scratch
- Image preprocessing and augmentation pipeline
- Training with callbacks (early stopping, model checkpointing)
- Inference script for single/batch predictions

## Result
The model has 87\9.78% Accuracy

## Requirements
- Python 3.8+
- See [requirements.txt](requirements.txt)

## Installation
```bash
git clone https://github.com/yourusername/hsr-map-classifier.git
cd hsr-map-classifier
pip install -r requirements.txt