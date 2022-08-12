# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The goal of this project is to create a model that can predict whether a loan application will be accepted or denied based on a set of features.

## Hypothesis
My hypotheses:
1. Applicants with a credit history will have a higher chance of being eligible for a loan
2. Applicants with more dependents
3. Applicants with higher education
4. Applicants with a high income/loan amount ratio

## EDA 
I found that the dataset included:
1. A higher ratio of males to females
2. A higher ratio of graduates
3. A higher ratio of married individuals
4. 2/3 of the loans were accepted

I found the following skews:
1. Income
2. income/loan ratio
3. loan ratio

With pivot plots I found:
1. Graduates had higher incomes and took out larger loans for longer, they were also more likely to have credit history
2. Females with 1 dependent had the highest incomes followed by males with 3+ dependents
3. Graduates had higher income and were more likely to get their loan approved
4. Applicants with high income and no credit history were most likely to get their loans approved

Note:
1. Credit history is not enough to determine if a loan will be approved because people can have a good or bad credit score greatly influencing 
their chances of approval.

## Process
(fill in what you did during EDA, cleaning, feature engineering, modeling, deployment, testing)
### EDA
During my EDA I graphed most of my data which can be seen in my instructions.ipynb notebook
### Cleaning
I replaced the following null values:
1. Credit History: '0' because I made the assumption that null values were more likely to represent 0 than 1
2. Self Employed: 'No' because most people in the dataset were employed in an organization
3. LoanAmount: 'Median' because the value could not be 0 and using the mean wouldn't be representative of the distribution due to outliers
4. Dependents: '0' because I made the assumption that null values are more likely to be 0 than > 1
5. Loan Amount Term: '360' because most loans were taken out for 360 days
6. Gender: 'Male' because they represented a larger proportion of the dataset
7. Married: 'No' because they represented a larger proportion of the dataset
### Feature engineering
1. Binary encoded Gender, Married, Education, Self Employed and Loan Status
2. Dummy coded Dependents and Property Area
3. Created a Income/LoanAmount ratio feature
### Modeling
For my modeling I created a pipeline that initially applied a log transform to my ratio, Income and Loan Amount columns because they showed a skew in my EDA. For my scaling I applied either StandardScaler or MinMaxScaler. I then added a Variance threshold to drop columns with too little variance. For my features a feature_union was created between pca or selectKbest. This was because this dataset had many features, but also some of the original features such as education and income also looked like great indicators of approval. Finally I applied a random forest, logistic regression or support vector classifier. I inserted my pipeline with my parameters into Gridsearch to find the best hyperparameters.
### Deployment
I saved my model with the best parameters using pickle and reused it in my app.py file in the src folder. Here I used flask and copied my classes needed for my pipeline. I then set up my api with /Approval as my endpoint. This will return to the user if they were approved or not based on the parameters that were given in the post request. 1 means they were accpeted while 0 means they were denied. The app was run for the local computer.
### Testing
I created a makeshift json dictionary from the first row of my final dataframe and used it as a test. I sent the dictionary with my post request and received the expected output; therefor, verifying it's validity.


## Results/Demo
(fill in your model's performance, details about the API you created, and (optional) a link to an live demo)
My model achieved a training accuracy of 0.75 and a test accuracy of 0.85 which I found was acceptable. The best hyperparameters were the following:
1. Classifier: Logistic Regression
2. PCA components: 3
3. Select K best: 3
4. scaler: MinMaxScaler
5. Variance Threshold: 0

My Api accepted a post request in json format with the following column names (ignore the values):
```
json_data = {
    'LoanAmount' : 128.0,
    'Loan_Amount_Term' : 360.0,
    'Credit_History' : 1.0,
    'Incomes' : 5849.0,
    'Income/LoanAmount_ratio' : 45.695312,
    'Gender_encoded' : 1,
    'Married_encoded' : 0,
    'Education_encoded' : 0,
    'Self_Employed_encoded' : 0,
    'Dependents_0' : 1,
    'Dependents_1' : 0,
    'Dependents_2' : 0,
    'Dependents_3+' : 0,
    'Property_Area_Rural' : 0,
    'Property_Area_Semiurban' : 0,
    'Property_Area_Urban' :  1  
}
```
## Challenges 
I faced challenges during my pipeline because I was still new to the concept of stringing classes together. Furthermore, it was difficult to understand how to implement custom classes such as the log transform I performed on my skewed distributions. Organizing files within my repo was also a difficulty, but that is probably because I've switched to windows for a bit. Accesing different files through jupyter notebook and vscode; however, did get confusing at times. It was also hard to keep track of all the components I was adding to my pipeline, model. Overall, it was a fun project and I wish I had more time to really play around with the features as my test score was promising.

## Future Goals
If I had more time I would add everything into my pipeline including my dummy, binary encoding. The json format I have to post to the api requires previous knowledge of what has been dummy coded and generates a non-friendly user interface. Idealy, I would have somebody input data in the format as the original dataframe and have the data prep and preprocessing executed in the pipeline. Furthermore, I would tweak my model more closely to drop columns that are least important. For example, if Income and Education were most important and accounted for the majority of the accuracy I would make those necessary parameters for the API. I would then make the other parameters optional. That would make the API user friendly and still possibly complex if the user desired a more accurate response.
