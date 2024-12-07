# Emotion Classification with Deep Learning
This project uses a Convolutional Neural Network (CNN) built in TensorFlow/Keras to classify human facial emotions into one of seven categories: angry, disgust, fear, happy, sad, surprise, and neutral. The dataset consists of images organized into folders by emotion, with preprocessing and training pipelines implemented in Python.

## Features
Data Loading: Efficiently loads images from a directory structure using TensorFlow's ImageDataGenerator.
Preprocessing: Images are resized to 48x48 and normalized to enhance model performance.
Model Architecture: A custom CNN designed to handle grayscale emotion classification.
Train/Validation/Test Split: The dataset is divided into training (70%), validation (15%), and testing (15%) sets.
Data Augmentation: Applies random transformations like rotation, shifting, and flipping to improve generalization.

## Installation
### 1. Clone this repository:
git clone https://github.com/yourusername/emotion-classification.git

### 2. Install dependencies:

pip install -r requirements.txt

### 3. Place the dataset in the dataset/ directory.

## Results
The model achieves approximately 65% accuracy on the test set Future improvements include:

Optimizing the CNN architecture.
Experimenting with different data augmentation techniques.

## Acknowledgments
Dataset used for the model training: https://www.kaggle.com/datasets/noamsegal/affectnet-training-data/data
