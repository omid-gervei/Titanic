# Titanic
<h1 id= "top doc"> Description </h1>

---




1. General info
In this project we have a database containing general information about the passengers of titanic.
The goal of the project is to forecast the aliveness status of the passengers using some infomation like: Age, Sex, ticket class, ...

2. Used methods

we used ***Grid search*** to find the best parameters of the most famous **machine learninig** algorithms:

- Decision Tree Classifier

- Random Forest

- XGBoost Classifier


# Highlights



 ```python

XGBC = XGBClassifier(colsample_bytree=1, gamma= 0, learning_rate= 0.1, max_depth=3,n_estimators=100,subsample=0.75,random_state = 1)
XGBC.fit(X_train,y_train)

 ```
And a the end we took advantage of ***Gradio*** for building a web app.




- link to some where <a href= "#top doc"> go to up </a>
