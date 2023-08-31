# Breast Cancer Detection

![Breast Cancer Detection Logo](images/logo.png)

Predicting breast cancer tumor malignancy through a Flask web application integrated with Docker.

## Overview

This project focuses on developing an accurate and scalable solution for breast cancer detection using a Flask web application and Docker. By employing various classification models and leveraging the power of Scikit-learn's Random Forest, the application predicts tumor malignancy with superior accuracy. The project showcases efficient data manipulation with Pandas and NumPy, and model storage using Joblib.

## Project Highlights

- **Web Application**: Created a user-friendly Flask web application for breast cancer detection, providing an intuitive interface for users to input data and receive predictions.

- **Docker Integration**: Orchestrated the deployment process using Docker, ensuring efficient containerization and making the application deployment-ready across different environments.

- **Predictive Modeling**: Employed a range of classification models to predict tumor malignancy. Notably, Scikit-learn's Random Forest was chosen for its exceptional accuracy.

- **Data Manipulation**: Utilized Pandas and NumPy libraries for precise data manipulation, ensuring high-quality input for the classification models.

- **Model Storage**: Employed Joblib to efficiently store and retrieve trained classification models, enabling quick predictions without retraining.

- **Scalability**: Ensured seamless scalability of the application through Docker, allowing easy adaptation to changing usage patterns and increased demand.

## Getting Started

1. Clone the repository: https://github.com/K-Charitharth/Breast_Cancer_Detection.git
2. Install the required dependencies: pip install -r requirements.txt
3. Run the Flask web application: python app.py
4. Access the application in your web browser at `http://localhost:5000`.

## Docker deployment
1. Docker build: docker build -t breast_cancer_detection:latest .
2. Run the container: docker run -d -p HOST_PORT:5000 breast_cancer_detection:latest

## License

This project is licensed under the [MIT License](LICENSE).

## Contributors

- Kothakota Charitharth

Feel free to contribute, provide feedback, or report issues.

