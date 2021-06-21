# Deploy Machine Learning Models with Django
(My machine learning webservices)

This web service makes Machine Learning models available with REST API. It is different from most of the tutorials available on the internet: 
1. it keeps information about many ML models in the web service. There can be several ML models available at the same endpoint with different versions. What is more, there can be many endpoint addresses defined. 
2. it stores information about requests sent to the ML models, this can be used later for model testing and audit.
3. it has tests for ML code and server code,
4. it can run A/B tests between different versions of ML models.


### The code structure 
In the <kbd>research</kbd> directory there are:
* code for training machine learning models on Adult-Income dataset [link](https://raw.githubusercontent.com/pplonski/datasets-for-start/master/adult/data.csv) 
* code for simulating A/B tests 

In the <kbd>backend</kbd> directory there is Django application.

In the <kbd>docker</kbd> directory there are dockerfiles for running the service in the container.


Markup : ![picture alt]("https://github.com/Kumar021/ml_web_services/blob/main/image/ml_algorithm_code.png")

Markup : ![picture alt]("https://github.com/Kumar021/ml_web_services/blob/main/image/ab_test.png")

Markup : ![picture alt]("https://github.com/Kumar021/ml_web_services/blob/main/image/api_endpoints.png")

Markup : ![picture alt]("https://github.com/Kumar021/ml_web_services/blob/main/image/Predict-%E2%80%93-result_endpoints.png")

Markup : ![picture alt](https://github.com/Kumar021/ml_web_services/blob/main/image/MLRequest-object-2-Change-ml-request-Django-site-admin.png")
![picture alt](http://via.placeholder.com/200x150 "Title is optional")
