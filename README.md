# ML Predict API Docker (simple)

This project serves as template project for an dockerized flask ML application.

## Random Forest Model
For demo purposes I used the iris data and build a random forest classification model that can predict 3 different types of irises: Setosa, Versicolour, and Virginica. The trainig code is under `model_train.py`.

## API
The API serves with two endpoints:
 1. localhost:5000/predict [GET]
 2. localhost:5000/predict_from_file [POST]

The api based on `flask`. For api testing and documentation swagger from `flasgger` is used. For more details look in the code.

## Docker
For launching the ml api with docker use the following commands:

 `cd ./api`
 `docker build -t iris_predict` 
 `docker run -p 0.0.0.0:5000:5000/tcp --name my_rl_iris_api iris_predict`  

*The last command starts a new docker container*


***
**Credentials**  
This project based on the udemy course Deploy Machine Learning & NLP Models with Dockers (DevOps): https://www.udemy.com/course/deploy-data-science-nlp-models-with-docker-containers/