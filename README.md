# Prediction On Input Image

https://github.com/Deepaklokesh612/Distracted-Driver-Detection-Using-Deep-Learning/assets/126693213/a90492c2-3adc-4993-b20f-3a3c3027cd5e

# Prediction On Input Video

https://github.com/Deepaklokesh612/Distracted-Driver-Detection-Using-Deep-Learning/assets/126693213/b8e29a07-268c-4c34-b63e-413924efe6cc

# Project Overview

This project aims to develop a system that detects distracted drivers using deep learning techniques. The system uses image classification to identify whether a driver is distracted and, if so, what type of distraction is occurring (e.g., texting, talking on the phone, eating, etc.). The application is built using a deep learning model for image classification and a web interface using Dash for user interaction.

# Problem Statement

Given a dataset of 2D dashboard camera images, an algorithm needs to be developed to classify each driver's behaviour and determine if they are driving attentively, wearing their seatbelt, or taking a selfie with their friends in the backseat etc..? This can then be used to automatically detect drivers engaging in distracted behaviours from dashboard cameras.

### Following are needed tasks for the development of an algorithm:

1) Download and preprocess the driver images

2) Build and train the model to classify the driver images

3) Test the model and further improve the model using different techniques.

# Approach 

## 1. Problem Definition

Distracted driving is a significant cause of road accidents. The goal of this project is to develop a system that can automatically detect whether a driver is distracted using images. The system should be able to classify images into different categories of distractions, such as texting, talking on the phone, eating, etc.

## 2. Data Collection
### 2.1. Dataset
Source: Use a publicly available dataset, such as the "State Farm Distracted Driver Detection" dataset from Kaggle.

Categories: The dataset should have labeled images of drivers in various states such as:

1) Safe driving

2) Texting (right/left)

3) Talking on the phone (right/left)

4) Operating the radio

5) Drinking

6) Reaching behind

7) Hair and makeup

8) Talking to passenger

## 3. Data Preprocessing
### 3.1. Data Augmentation
Techniques: Apply random transformations to increase the diversity of the training data. Common techniques include:
Horizontal flipping
Random cropping
Rotation
Scaling
Brightness and contrast adjustment

### 3.2. Normalization
Normalize pixel values to a range suitable for the model (e.g., [0, 1]).

## 4. Model Selection
### 4.1. Convolutional Neural Networks (CNNs)
CNNs are highly effective for image classification tasks due to their ability to capture spatial hierarchies in images.
Consider using pre-trained models like VGG16, ResNet50, or MobileNetV2, which can be fine-tuned for this specific task.

## 5. Model Training
### 5.1. Transfer Learning
Pre-trained Models: Use pre-trained weights from models trained on large datasets like ImageNet.
Fine-tuning: Fine-tune the model on the distracted driver dataset. This involves freezing some of the initial layers and training the last few layers on the new dataset.

### 5.2. Custom Model
Alternatively, design a custom CNN architecture tailored to the dataset.

### 5.3. Hyperparameter Tuning
Experiment with different learning rates, batch sizes, and optimizers (e.g., Adam, SGD).
Use techniques like cross-validation to find the optimal set of hyperparameters.

## 6. Evaluation
### 6.1. Metrics
Use metrics like accuracy, precision, recall, and F1-score to evaluate the model's performance.
Plot confusion matrices to understand the misclassification patterns.

### 6.2. Validation
Split the data into training, validation, and test sets.
Monitor performance on the validation set to avoid overfitting.

## 7. Deployment
### 7.1. Web Interface
Framework: Use Dash to create a web application.
Functionality:
Upload image files.
Display uploaded images.
Classify the images and display results.

# Model Details

The deep learning model used for this project is a pre-trained convolutional neural network (CNN) and VGG16 fine-tuned for the task of distracted driver detection. The model is capable of classifying images into multiple categories based on the type of distraction.

# Usage

1) Upload Image: Drag and drop or select an image file of a driver.

2) Classify: Click on the "Classify" button to get the prediction.

3) View Results: The application will display the uploaded image and the classification results.

# Prerequisites

1) Python 3.10
2) Required Python packages: Install with pip install -r requirements.txt
3) Dataset: Download the dataset from [[Link](https://www.kaggle.com/competitions/state-farm-distracted-driver-detection/data?select=imgs)] and place it in the appropriate directory.

# Acknowledgements
The project is inspired by the need for road safety and reducing accidents caused by distracted driving.

Special thanks to the open-source community for providing valuable resources and tools.
