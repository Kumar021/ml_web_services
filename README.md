# Deploy Machine Learning Models with Django
My machine learning webservices

This web service makes Machine Learning models available with REST API. It is different from most of the tutorials available on the internet: 
1. it keeps information about many ML models in the web service. There can be several ML models available at the same endpoint with different versions. What is more, there can be many endpoint addresses defined. 
2. it stores information about requests sent to the ML models, this can be used later for model testing and audit.
3. it has tests for ML code and server code,
4. it can run A/B tests between different versions of ML models.
