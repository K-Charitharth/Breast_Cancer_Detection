# Breast Cancer Detection Web Application
This is a web application for breast cancer detection using a pre-trained machine learning model. The app is built with Flask and can be deployed using Docker.

Table of Contents
Description
Requirements
Installation
Usage
Docker Deployment
Authors
License
Description
The web application allows users to input various features related to breast cancer tumors, and it uses a pre-trained Random Forest model to predict whether the tumor is malignant or benign.

The application uses the following technologies:

Flask: A Python web framework for building web applications.
Scikit-learn: A machine learning library for building and training the Random Forest model.
Docker: A platform for building, shipping, and running applications in containers.
Requirements
Python 3.8 or later
Docker

# Docker deployment
Docker build: docker build -t breast_cancer_detection:latest .
Run the container: docker run -d -p HOST_PORT:5000 breast_cancer_detection:latest



# Author
Kothakota Charitharth

