# Honkai Star Rail Map Classifier

A CNN model that classifies game map areas from Honkai Star Rail into three categories: Herta Space Station, Jarilo-VI, and The Luofu.

## Features
- Custom CNN model trained from scratch
- Image preprocessing and augmentation pipeline
- Training with callbacks (early stopping, model checkpointing)
- Inference script for single/batch predictions

## Result
The model has 89.78% Accuracy on test set

## Requirements
- Python 3.8+
- See [requirements.txt](requirements.txt)

## Clone
```bash
git clone https://github.com/fslmc/hsr-map-classifier.git
cd hsr-map-classifier
pip install -r requirements.txt
